from motor.motor_asyncio import AsyncIOMotorClient
from config import database_config, bot_config
from security import block_database as block_db
from app.keyboards import main_showNewsKb
import time

serverConnect = AsyncIOMotorClient('127.0.0.1', 27017)
main_db = serverConnect['nt_BotUsers']
nt_users = main_db['nt_users']
nt_blocked = main_db['nt_blocked']


async def main_initBotDatabase(colls: dict[str]):
    for database, index in database_config.collsUsers:
        coll_mainDB = main_db[database]
        news_mainDB = main_db['nt_news']
        main_indexConnect = await coll_mainDB.create_index((f'{index}', 1))
    else:
        return 'databaseBot 200 ok.'
async def main_WriteNews(user_id: int, text: str, title: str):
    if user_id in bot_config.admin_user:
        newsDB = main_db['nt_news']
        timestamp = time.time()  # текущее время в секундах (float)
        readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

        await newsDB.insert_one({
            'from': 'admin',
            'title': title,
            'message': text,
            'timestamp': readable
        })
        return readable
    else:
        return None
    
async def main_getNews():
    newsDB = main_db['nt_news']
    last_news = newsDB.find({}, {'_id': False, 'title': 1}).sort('$natural', -1).limit(5)

    news_titles = []
    async for doc in last_news:
        if 'title' in doc:
            news_titles.append(doc['title'])

    return await main_showNewsKb(news_titles)

async def main_getNew(title: str):
    news_DB = main_db['nt_news']
    document = await news_DB.find_one({'title': title}, projection={'_id': False})
    if document:
        return document['title'], document['message'], document['timestamp']
    else:
        return None, None, None

async def main_registerUser(user_id: int, lang: str = 'ru'):
    if len(str(user_id)) > 4:
        main_doc = await block_db.main_GetWalletUser(user_id=user_id)
        if main_doc is not None:
            bot_doc = {
                'user_id': user_id,
                'status': 'active',
                'wallet_address': main_doc['wallet_address'],
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
        print(user_data)
        return user_data
    else:
        return None