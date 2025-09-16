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
            
async def main_searchUser(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/search', json={
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
            
async def main_generateInvouce(from_user_id: int, amount: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/regInvouce', json={
            'user_id_sender': from_user_id,
            'amount': amount
        }) as response:
            data = await response.json()
            if data is not None:
                if data.get('status', '').lower() == 'generated':
                    uid = data.get('invouce_UID', '')
                    from_user = data.get('user_id_sender', '')
                    return uid, from_user
                else:
                    return None, None
            else:
                return None, None
async def main_deleteInvouce():
    pass