import aiohttp
from config import database_config
from utils import api_getter

temp_key: str | None = None  # глобальная переменная

async def init_temp_key():
    global temp_key
    temp_key = await api_getter.main_gettempKey()

async def main_GetWalletUser(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/reg', json = {
        'user_id': f'{user_id}'
    }) as response:
            data = await response.json()
            if data:
                if data.get('wallet_address', None):
                    return data
                else:
                    return None
            else:
                return None