from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from security.config import user_checks, database
from security import database as dbs
import uuid

client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']
lgg_dbs = mainClient[user_checks]
main_db = mainClient[database]

async def loggCheck(wallet_from: str, amount: float):
    UID_TRSCTN = f'CHECK{uuid.uuid4()}'
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
    try:
        transaction_dataByID = await lgg_dbs.find_one({'CHECK_ID': tx_UID})
        if transaction_dataByID and transaction_dataByID["status"] == 1:
            amount_to_add = transaction_dataByID["amount"]
            await lgg_dbs.update_one({'CHECK_ID': tx_UID}, {'$set': {'status': 2}})
        
            sender_dataByWallet = await dbs.main_searchUserwallet(wallet_address=transaction_dataByID['wallet_from'])
            if sender_dataByWallet and sender_dataByWallet['balance'] > amount_to_add:
                await main_db.update_one({'user_id': user_recipient_id}, {'$inc': {'balance': amount_to_add}})
                await main_db.update_one({'user_id': sender_dataByWallet['user_id']}, {'$inc': {'balance': -amount_to_add}})
            
                user_recipientBalance = await main_db.find_one({'user_id': user_recipient_id})
                user_recipientBalance["_id"] = str(user_recipientBalance['_id'])
                return user_recipientBalance["balance"], transaction_dataByID['wallet_from']
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None



async def loggDelete(wallet_sender_id: int, check_UID: str, user_id: int):
    check_data = await lgg_dbs.find_one(
        {'CHECK_ID': check_UID},
        projection={'_id': False}
    )

    if not check_data:

        return None

    if check_data.get('wallet_from') != wallet_sender_id or check_data.get('status') == 2:

        return None

    deleted_data = await lgg_dbs.find_one_and_update(
        {'wallet_from': wallet_sender_id, 'CHECK_ID': check_UID},
        {'$set': {'status': 2}},
        projection={'_id': False},
        return_document=ReturnDocument.AFTER
    )
    back_money = await main_db.find_one_and_update({'user_id': user_id}, {'$inc': {'balance': check_data['amount']}})
    return deleted_data

async def search_check(UID: str):
    data = await lgg_dbs.find_one({'CHECK_ID': UID}, projection={'_id': False})
    if data is not None:
        print(data)
        return data
    else:
        return None