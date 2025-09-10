from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties as prop
import config.bot_config as conf
from app.handlers import router
import asyncio
from security.block_database import init_temp_key

bot = Bot(token=conf.BOT_TOKEN, default=prop(parse_mode='HTML', link_preview_prefer_large_media=True))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await init_temp_key()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())