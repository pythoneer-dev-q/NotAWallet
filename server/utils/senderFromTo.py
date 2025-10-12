from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from security.config import user_checks, database
from security import database as dbs
import uuid


async def send_funds(from_wallet: str, to_wallet: str):
    pass