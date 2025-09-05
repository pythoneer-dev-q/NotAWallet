from motor.motor_asyncio import AsyncIOMotorClient
from security.config import database_transactions
import uuid

client = AsyncIOMotorClient('127.0.0.1', 27017)
mainClient = client['NotAwallet']
lgg_dbs = mainClient[database_transactions]

async def loggTransaction(wallet_from: str, wallet_to: str, amount: float):
    UID_TRSCTN = f'{uuid.uuid4()}NT{uuid.uuid4()}'
    trsctn_doc = {
        'wallet_from': wallet_from,
        'wallet_to': wallet_to,
        'amount': amount,
        'TX_ID': UID_TRSCTN
    }
    check_row = await lgg_dbs.insert_one(trsctn_doc)
    trsctn_doc["_id"] = str(trsctn_doc['_id'])
    return trsctn_doc