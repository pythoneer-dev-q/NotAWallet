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
async def main_deleteInvouce(clicked_user_id: int, invouce_UID: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/deleteInvouce', json={
            'user_id': clicked_user_id,
            'UID': invouce_UID
        }) as response:
            data = await response.json()
            if data is not None:
                if data.get('status', '').lower() == 'deleted':
                    amount = data['transaction_doc']['amount']
                    from_user = data['transaction_doc']['user_id']
                    status = 'finished' if data['transaction_doc']['status'] == 2 else 'not_finished'
                    return status, from_user, amount
                else:
                    return None, None, None
            else:
                return None, None, None



async def main_generateCheck(from_user_id: int, amount: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/regCheck', json={
            'user_id': from_user_id,
            'amount': amount
        }) as response:
            data = await response.json()
            if data is not None:
                if data.get('status', '').lower() == 'generated':
                    tx_uid = data['tx_UID']
                    from_user_wallet = data['wallet_sender']
                    return tx_uid, from_user_wallet, amount
                else:
                    return None, None, None
            else:
                return None, None, None
            
async def main_deleteCheck(clicked_user_id: int, invouce_UID: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/delCheck', json={
            'user_id_clicker': clicked_user_id,
            'UID': invouce_UID
        }) as response:
            data = await response.json()
            if data is not None:
                if data.get('deleted_user', '') is not None:
                    amount = data['transaction_doc']['amount']
                    wallet_from = data['transaction_doc']['wallet_from']
                    check_uid = data['transaction_doc']['CHECK_ID']
                    return amount, wallet_from, check_uid, clicked_user_id
                else:
                    return None, None, None, None
            else:
                return None, None, None, None
            
async def main_searchInvouce(invouce_uid: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/searchInvouce', json={
            'invouce_UID': invouce_uid
        }) as response:
            data = await response.json()
            if data.get('status', '') is not None:
                from_user = data['document']['user_id']
                amount = data['document']['amount']
                UID = data['document']['UID']
                status = 'NT' if data['document']['status'] == 1 else 'USED'
                return from_user, amount, UID, status
            else:
                return None, None, None, None