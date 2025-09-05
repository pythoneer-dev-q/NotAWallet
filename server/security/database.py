from motor.motor_asyncio import AsyncIOMotorClient
from uuid import uuid5
from config import (
    database, database_transactions, MAIN_DATABASE, limited_users, user_checks, user_invouces,
    collection_list
)
client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']

async def init():
    try:
        client = AsyncIOMotorClient('127.0.0.1', 27017)
        mainClient = client['NotAwallet']
        for collection in collection_list:
            all_db = mainClient[collection]
            await all_db.create_index()
        print('database ok. 200.')
        return
    except:
        print('база данных не инициализированна. проверьте подключение к серверу.')
        raise KeyError()
    
# поиск пользователя (используется проиндексированное поле "user_id" -> см. "security/config")
async def main_searchUser(user_id: int):
    registered_db = mainClient[database]
    pattern = {'user_id': user_id}
    user_byId = registered_db.find_one(pattern)
    if user_byId:
        return user_byId
    else:
        return None
    
# регистрация пользователя (если не зарегистрирован)
async def main_registerUser(user_id: int, meta: str = None):
    register_db = mainClient[database]
    UID = uuid5()
    main_doc = {
        'wallet_address': f'{UID}',
        'user_id': int(user_id),
        'balance': 0.0,
        'meta': ''
    }
    if (len(user_id) >= 4) and (main_searchUser(user_id) is None):
        await register_db.insert_one(main_doc)
        return main_doc
    else:
        return None


async def main_registerTransactions(user_id: int):
    pass

async def main_limiterUser(user_id: int):
    pass

async def main_registerInvoucees(user_id: int):
    pass

async def main_registerChecks(user_id: int):
    pass