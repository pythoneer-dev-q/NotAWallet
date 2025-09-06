from pydantic import BaseModel

class RegUser(BaseModel):
    user_id: int

class SendToWallet(BaseModel):
    user_id: int
    wallet_address: str
    amount: float

class RegCheck(BaseModel):
    user_id: int
    amount: float

class GetCheck(BaseModel):
    user_id_recipient: int
    tx_UID: str