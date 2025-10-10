from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse as jsresp
import time
import uvicorn
import security.database as db
import security.config as conf
from utils.models import (
    RegUser, SendToWallet, RegCheck, GetCheck, RegInvouce, GetInvouce, SearchUser, DeleteInvouce, DelCheck, SearchCheckRequest, SearchInvouceRequest,
    SearchWallet
)


app = FastAPI()

@app.get('/')
@app.get('/main_server')
async def main_helloWorld():
    return jsresp({
        'detail': 'OK.',
        'time': f'{time.time()}'
    })
@app.post('/search')
async def main_searchuserData(user_insertData: SearchUser):
    user_walletData = await db.main_searchUser(user_id=user_insertData.user_id)
    if user_insertData is not None:
        return jsresp(content=user_walletData, status_code=200)
    else:
        return jsresp(content={
            'status': 'error',
            'detail': 'not found'
        }, status_code=404)
    
@app.post('/searchWallet')
async def main_searchByWallet(user_ByWallet: SearchWallet):
    if user_ByWallet.wallet.startswith('NOTWLT'):
        data = await db.main_searchUserwallet(wallet_address=user_ByWallet.wallet)
        if (data is not None) and (data is not False):
            return jsresp(content={'data': data}, status_code=200)
        else:
            return jsresp(content={'detail': 'CM /errs'}, status_code=404)


@app.post('/send')
async def main_SenderWallet(tx_user: SendToWallet):
    loggedData = await db.main_registerTransactions(tx_user.user_id,sum_sending=tx_user.amount, recipient=tx_user.wallet_address)
    if loggedData in conf.errs_transactions:
        return jsresp({'error': loggedData, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'Transfered', 'logged_tr': loggedData}, 200)
    
@app.post('/regCheck')
async def main_RegisterChecks(check_user: RegCheck):
    tx_UID, from_wallet = await db.main_registerCheck(check_user.user_id, check_user.amount)
    if tx_UID in conf.errs_transactions:
        return jsresp({'error': tx_UID, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'Generated', 'tx_UID': tx_UID, 'wallet_sender': from_wallet}, 200)     
       
@app.post('/getCheck')
async def main_CheckGetter(check_getter: GetCheck):
    UID, balance, user_id, wallet_from, status = await db.main_handlerActivateCheck(to_user_id=check_getter.user_id_recipient, tx_UID=check_getter.tx_UID)
    if UID in conf.errs_transactions:
        return jsresp({'error': UID, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': status, 'wallet_from': wallet_from, 'tx_UID': UID, 'after_balance': balance, 'activated_user': user_id}, 200)    
@app.post('/delCheck')
async def main_CheckDeleter(check_deleter: DelCheck):
    transaction_data = await db.main_deleterCheck(from_user_id=check_deleter.user_id_clicker, inv_UID=check_deleter.UID)
    if transaction_data in conf.errs_transactions:
        return jsresp({'error': transaction_data, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'transaction_doc': transaction_data, 'deleted_user': check_deleter.user_id_clicker}, 200)    

@app.post('/searchCheck')
async def main_check_searcher(user_clicked_data: SearchCheckRequest):
    data = await db.main_searchCheck(check_UID=user_clicked_data.check_UID)
    if data in conf.errs_transactions:
        return jsresp({'error': data, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'found', 'document': data}, 200)    


@app.post('/regInvouce')
async def main_InvouceRegister(invouce_sender: RegInvouce):
    info, UID = await db.main_registerInvouces(from_user_id=invouce_sender.user_id_sender, amount=invouce_sender.amount)
    if info in conf.errs_transactions:
        return jsresp({'error': info, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'Generated', 'invouce_UID': UID, 'user_id_sender': invouce_sender.user_id_sender}, 200)     

@app.post('/getInvouce')
async def main_invouceGetter(invouce_getter: GetInvouce):
    doc_trn, info_payeer = await db.main_handlerInvouces(payeer_user_id=invouce_getter.user_id_sender, invouce_UID=invouce_getter.UID)
    if doc_trn in conf.errs_transactions:
        return jsresp({'error': doc_trn, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'Paid', 'transaction_doc': doc_trn, 'user_payeer_info': info_payeer}, 200) 
        
@app.post('/deleteInvouce')
async def main_invouceDeleter(invouce_deleterData: DeleteInvouce):
    data = await db.main_deleterInvouce(user_idCreator=invouce_deleterData.user_id, invouce_UID=invouce_deleterData.UID)
    if data in conf.errs_transactions:
        return jsresp({'error': data, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'deleted', 'transaction_doc': data}, 200)     
@app.post('/searchInvouce')
async def main_invouce_searcher(user_clicked_data: SearchInvouceRequest):
    data = await db.main_searchInvouce(invouce_UID=user_clicked_data.invouce_UID)
    if data in conf.errs_transactions:
        return jsresp({'error': data, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'found', 'document': data}, 200)    



@app.post('/register')
@app.post('/reg')
async def main_registerUser(user: RegUser, request: Request):
    user_id = user.user_id
    reg_doc = await db.main_registerUser(int(user_id), meta=request.headers)
    if  reg_doc is not None:
        return reg_doc
    else:
        return jsresp({'error': 'user already have registered'}, 403)