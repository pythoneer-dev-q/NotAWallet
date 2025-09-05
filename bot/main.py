from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio

bot = Bot()
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())