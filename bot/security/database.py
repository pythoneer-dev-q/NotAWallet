from motor.motor_asyncio import AsyncIOMotorClient
from config import database_config
from security import block_database as block_db

serverConnect = AsyncIOMotorClient('127.0.0.1', 27017)
main_db = serverConnect['nt_BotUsers']
nt_users = main_db['nt_users']
nt_blocked = main_db['nt_blocked']


async def main_initBotDatabase(colls: dict[str]):
    for database, index in database_config.collsUsers:
        coll_mainDB = main_db[database]
        main_indexConnect = await coll_mainDB.create_index((f'{index}', 1))
    else:
        return 'databaseBot 200 ok.'
    

async def main_registerUser(user_id: int, lang: str = 'ru'):
    if len(str(user_id)) > 4:
        main_doc = await block_db.main_GetWalletUser(user_id=user_id)
        if main_doc is not None:
            bot_doc = {
                'user_id': user_id,
                'status': 'active',
                'block_info': main_doc,
                'node': '',
                'lang': f'{lang}'
            }
            resisteruser = await nt_users.insert_one(bot_doc)
            bot_doc['_id'] = str(bot_doc['_id'])
            return bot_doc
        else:
            return None
    else:
        return None

async def main_searchUser(user_id: int):
    user_data = await nt_users.find_one({'user_id': user_id})
    if (user_data is not None) and (user_data['status'] != 'blocked'):
        user_data['_id'] = str(user_data['_id'])
        return user_data
    else:
        return None