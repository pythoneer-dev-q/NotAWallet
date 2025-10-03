import uvicorn 
import asyncio
from app.handlers import app
from security import database
from assets.api_handler import asset_app
# инициализация используя запрос к init() в database.py,
# создает коллекции и индексы, если их нет, если есть -- индексирует по asc (1)

app.include_router(asset_app)

async def main():
    try:
        await database.init()
        return 1
    except:
        return KeyError
    
# головной запуск

if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run(app, host='127.0.0.1', port=8001)