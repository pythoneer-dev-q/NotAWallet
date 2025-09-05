from pydantic import BaseModel

class RegUser(BaseModel):
    user_id: int

class SendToWallet(BaseModel):
    user_id: int
    wallet_address: str
    amount: float