from motor.motor_asyncio import AsyncIOMotorClient
from security.config import database, user_invouces
from utils import loggerTransactions
from uuid import uuid4


client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']
lgg_dbs = mainClient[user_invouces]
main_db = mainClient[database]

async def main_RegisterInvouce(user_id: int, amount: float):
    UID_invouce = f'INVC{uuid4()}'
    trnsctn_doc = {
        'user_id': user_id,
        'amount': amount,
        'UID': UID_invouce,
        'status': 1
    }
    insert_inf = await lgg_dbs.insert_one(trnsctn_doc)

    trnsctn_doc['_id'] = str(trnsctn_doc['_id'])
    return trnsctn_doc, UID_invouce


async def main_invouceHandler(payeer_user_id: int, amount: float, invouce_UID: str):
    invouce_data = await lgg_dbs.find_one({'UID': invouce_UID})
    payeer_data = await main_db.find_one({'user_id': payeer_user_id})
    recipient_data = await main_db.find_one({'user_id': invouce_data['user_id']})

    if (invouce_data) and (invouce_data["status"] == 1):
        user_decrBalance = await main_db.update_one({'user_id': payeer_user_id}, {'$inc': {'balance': -amount}})
        user_updBalance = await main_db.update_one({'user_id': invouce_data['user_id']}, {'$inc': {'balance': amount}})
        update_invouceBalance = await lgg_dbs.update_one({'UID': invouce_UID}, {'$set': {'status': 2}})

        main_doc = await loggerTransactions.loggTransaction(wallet_from=payeer_data['wallet_address'], wallet_to=recipient_data['wallet_address'], amount=amount)
        if main_doc:
            return main_doc, payeer_data
        else:
            return 'SRVR_ERR', None
    else:
        return 'ACTIVATED', None
    

async def main_validateInvouce(invouce_UID: str):
    invouce_data = await lgg_dbs.find_one({'UID': invouce_UID})
    if invouce_data:
        return invouce_data
    else:
        return None