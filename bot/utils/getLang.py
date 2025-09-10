from security.database import main_searchUser

async def main_getLang(user_id: int):
    user_data = await main_searchUser(user_id=user_id)
    user_data['_id'] = str(user_data['_id'])
    return user_data['lang']