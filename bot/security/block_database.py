import aiohttp
from config import database_config
from utils import api_getter

temp_key: str | None = None  # глобальная переменная

async def init_temp_key():
    global temp_key
    temp_key = await api_getter.main_gettempKey()

async def main_GetWalletUser(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/reg', json={
            'user_id': f'{user_id}'
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'wallet_address' in data:
                return data
            else:
                return None

async def main_searchUser(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/search', json={
            'user_id': f'{user_id}'
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'wallet_address' in data:
                return data
            else:
                return None

async def main_generateInvouce(from_user_id: int, amount: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/regInvouce', json={
            'user_id_sender': from_user_id,
            'amount': amount
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and data['status'].lower() == 'generated':
                uid = data.get('invouce_UID', '')
                from_user = data.get('user_id_sender', '')
                return uid, from_user
            else:
                return None, None

async def main_deleteInvouce(clicked_user_id: int, invouce_UID: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/deleteInvouce', json={
            'user_id': clicked_user_id,
            'UID': invouce_UID
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and data['status'].lower() == 'deleted':
                if 'transaction_doc' in data:
                    amount = data['transaction_doc']['amount']
                    from_user = data['transaction_doc']['user_id']
                    status = 'finished' if data['transaction_doc']['status'] == 2 else 'not_finished'
                    return status, from_user, amount
            return None, None, None

async def main_generateCheck(from_user_id: int, amount: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/regCheck', json={
            'user_id': from_user_id,
            'amount': amount
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and data['status'].lower() == 'generated':
                tx_uid = data['tx_UID']
                from_user_wallet = data['wallet_sender']
                return tx_uid, from_user_wallet, amount
            else:
                return None, None, None

async def main_deleteCheck(clicked_user_id: int, invouce_UID: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/delCheck', json={
            'user_id_clicker': clicked_user_id,
            'UID': invouce_UID
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'deleted_user' in data:
                if 'transaction_doc' in data:
                    amount = data['transaction_doc']['amount']
                    wallet_from = data['transaction_doc']['wallet_from']
                    check_uid = data['transaction_doc']['CHECK_ID']
                    return amount, wallet_from, check_uid, clicked_user_id
            return None, None, None, None

async def main_searchInvouce(invouce_uid: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/searchInvouce', json={
            'invouce_UID': invouce_uid
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and 'document' in data:
                from_user = data['document']['user_id']
                amount = data['document']['amount']
                UID = data['document']['UID']
                status = 'NT' if data['document']['status'] == 1 else 'USED'
                return from_user, amount, UID, status
            else:
                return None, None, None, None

async def main_searchCheck(check_uid: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/searchCheck', json={
            'check_UID': check_uid.replace('chk', '')
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and 'document' in data:
                from_user = data['document']['wallet_from']
                amount = data['document']['amount']
                UID = data['document']['CHECK_ID']
                status = 'NT' if data['document']['status'] == 1 else 'USED'
                return from_user, amount, UID, status
            else:
                return None, None, None, None

async def main_makeGetCheck(user_recipient: int, check_uid: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/getCheck', json={
            "user_id_recipient": user_recipient,
            "tx_UID": check_uid
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and 'wallet_from' in data:
                from_user, after_sender_balance = await main_searchByWallet(wallet=data['wallet_from'])
                user = data['activated_user']
                after_balance = data['after_balance']
                status = data['status']
                return from_user, user, after_balance, check_uid, status
            else:
                return None, None, None, None, None

async def main_makePayUser(user_id: int, invouce_uid: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/getInvouce', json={
            'UID': invouce_uid,
            'user_id_sender': user_id
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'status' in data and data['status'] == 'Paid':
                if 'transaction_doc' in data:
                    from_user = data['transaction_doc']['wallet_to']
                    from_user_id, from_user_idBalanceAfter = await main_searchByWallet(wallet=from_user)
                    amount = data['transaction_doc']['amount']
                    return from_user_id, from_user_idBalanceAfter, amount, invouce_uid
            return None, None, None, None

async def main_searchByWallet(wallet: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{database_config.API_URI}/searchWallet', json={
            'wallet': wallet
        }) as response:
            data = await response.json()
            if isinstance(data, dict) and 'data' in data:
                wallet_user = data['data']['user_id']
                user_balance = data['data']['balance']
                return wallet_user, user_balance
            else:
                return None, None
