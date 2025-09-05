import uvicorn 
import asyncio
from app.handlers import app


async def main():
    asyncio.create_task()
    uvicorn.run(app, host='127.0.0.1', port=8001)
