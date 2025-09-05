from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse as jsresp
import time
import uvicorn
import security.database as db
import security.config as conf
from utils.models import (
    RegUser, SendToWallet
)


app = FastAPI()

@app.get('/')
@app.get('/main')
async def main_helloWorld():
    return jsresp({
        'detail': 'OK.',
        'time': f'{time.time()}'
    })

@app.post('/send')
async def main_SenderWallet(tx_user: SendToWallet):
    loggedData = await db.main_registerTransactions(tx_user.user_id,sum_sending=tx_user.amount, recipient=tx_user.wallet_address)
    if loggedData in conf.errs_transactions:
        return jsresp({'error': loggedData, 'detail': 'см. /errs'}, 503)
    else:
        return jsresp({'status': 'Transfered', 'logged_tr': loggedData}, 200)




@app.post('/register')
@app.post('/reg')
async def main_registerUser(user: RegUser, request: Request):
    user_id = user.user_id
    reg_doc = await db.main_registerUser(user_id, meta=request.headers)
    if  reg_doc is not None:
        return reg_doc
    else:
        return jsresp({'error': 'user already have registered'}, 403)