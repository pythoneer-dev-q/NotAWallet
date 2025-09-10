from motor.motor_asyncio import AsyncIOMotorClient

api_DataBase = AsyncIOMotorClient('127.0.0.1', 27017)
api_db = api_DataBase['NotAwallet']
api_coll = api_db['API_KEY']

async def main_gettempKey():
    return await api_coll.find_one({})