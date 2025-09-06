from motor.motor_asyncio import AsyncIOMotorClient
from security.config import user_invouces, database
import uuid

client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']
lgg_dbs = mainClient[user_invouces]
main_db = mainClient[database]

async def loggCheck(wallet_from: str, amount: float):
    UID_TRSCTN = f'{uuid.uuid4()}CHECK{uuid.uuid4()}'
    trsctn_doc = {
        'wallet_from': wallet_from,
        'amount': amount,
        'CHECK_ID': UID_TRSCTN, 
        'status': 1
    }
    check_row = await lgg_dbs.insert_one(trsctn_doc)
    trsctn_doc["_id"] = str(trsctn_doc['_id'])
    return trsctn_doc["CHECK_ID"], trsctn_doc["wallet_from"]

async def loggUpdate(user_recipient_id: int, tx_UID: str):
    transaction_dataByID = await lgg_dbs.find_one({'CHECK_ID': tx_UID})
    if transaction_dataByID and transaction_dataByID["status"] == 1:
        amount_to_add = transaction_dataByID["amount"]
        await lgg_dbs.update_one({'CHECK_ID': tx_UID}, {'$set': {'status': 2}})

        adding_userRecipient = await main_db.update_one({'user_id': user_recipient_id}, {'$inc': {'balance': amount_to_add}})
        user_recipientBalance =await  main_db.find_one({'user_id': user_recipient_id})
        user_recipientBalance["_id"] = str(user_recipientBalance['_id'])

        return user_recipientBalance["balance"]
    else:
        return 0