from motor.motor_asyncio import AsyncIOMotorClient
from uuid import uuid4
from security.config import (
    database, database_transactions, MAIN_DATABASE, limited_users, user_checks, user_invouces,
    collection_list
)
from utils import loggerTransactions, loggerInvouces, loggerChecks

client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']

async def init():
    try:
        client = AsyncIOMotorClient('127.0.0.1', 27017)
        mainClient = client['NotAwallet']
        for collection in collection_list:
            all_db = mainClient[collection]
            await all_db.create_index([('user_id', 1), ('wallet_address', 1), ('CHECK_ID', 1), ('INVOUCE_ID', 1)])
        print('database ok. 200.')
        return
    except:
        print('база данных не инициализированна. проверьте подключение к серверу.')
        raise KeyError()
    
# поиск пользователя (используется проиндексированное поле "user_id" -> см. "security/config")
async def main_searchUser(user_id: int):
    registered_db = mainClient[database]
    pattern = {'user_id': user_id}
    user_byId = await registered_db.find_one(pattern)
    if user_byId is not None:
        return user_byId
    else:
        return None
#поиск пользователя по кошельку (нужно для переводов по внутренней системе -- без чеков)
async def main_searchUserwallet(wallet_address: str):
    registered_db = mainClient[database]

    if wallet_address.startswith('NOTWLT'):
        user_data = await registered_db.find_one({'wallet_address': f'{wallet_address}'})
        if user_data is not None:
            user_data["_id"] = str(user_data["_id"])
            return user_data
        else:
            return None
    else:
        return False

# регистрация пользователя (если не зарегистрирован)
async def main_registerUser(user_id: int, meta: str = None):
    register_db = mainClient[database]
    UID = f'NOTWLT{uuid4()}'
    main_doc = {
        'wallet_address': f'{UID}',
        'user_id': int(user_id),
        'balance': 0.0,
        'meta': ''
    }
    user_found = main_searchUser(user_id)
    if await user_found is None:
        await register_db.insert_one(main_doc)
        main_doc["_id"] = str(main_doc["_id"])
        return main_doc
    else:
        return None


async def main_registerTransactions(user_id: int, sum_sending: float, recipient: str):
    registered_db = mainClient[database]
    user_data = await main_searchUser(user_id)

    if user_data and user_data["balance"] < sum_sending:
        return 'SUM_ERR'
    else:
        data_UserbyWallet = await main_searchUserwallet(recipient)
        if (user_data is not None) and (data_UserbyWallet is not False):
            data_sendingUser = await registered_db.update_one({'user_id': user_id}, {'$inc': {'balance': -sum_sending}})
            data_recipientUser = await registered_db.update_one({'wallet_address': recipient}, {'$inc': {'balance': sum_sending}})
            data_loggedInto = await loggerTransactions.loggTransaction(wallet_from=user_data["wallet_address"], wallet_to=recipient, amount=sum_sending)
            
            if data_sendingUser and data_recipientUser and data_loggedInto:
                return data_loggedInto
            else:
                return 'SRVR_ERR'
        else:
            return 'WLT_NT_EXST'



    



async def main_limiterUser(user_id: int):
    pass

async def main_registerInvoucees(from_user_id: int, amount: float):
    registered_db = mainClient[database]

    sender_data = await main_searchUser(user_id=from_user_id)
    if (sender_data is not None):
        sender_balance = sender_data["balance"]
        sender_wallet = sender_data["wallet_address"]
        if sender_balance >= amount:
            decr_balance = await registered_db.update_one({'user_id': from_user_id}, {'$inc': {'balance': -amount}})
            tx_UID = await loggerInvouces.loggCheck(wallet_from=sender_wallet, amount=amount)
            return tx_UID
        else:
            return 'SUM_ERR', None
    else:
        return 'USER_ERR', None




async def main_handlerActivateCheck(to_user_id: int , tx_UID: str):    
    recipient_data = await main_searchUser(user_id=to_user_id)
    if recipient_data is not None:
        bill_info = await loggerInvouces.loggUpdate(user_recipient_id=to_user_id, tx_UID=tx_UID)
        if bill_info:
            return tx_UID, bill_info, to_user_id, 2
        else:
            return 'ACTIVATED', None,None, 0


async def main_registerChecks(user_id: int):
    pass