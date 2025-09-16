from security import block_database as bdb

async def main_sortuserData(lang: str, user_data: dict):
    user_data_block = await bdb.main_searchUser(user_id=user_data['user_id'])
    user_balance = user_data_block.get('balance', 0)
    user_status = user_data['status']
    user_wallet = user_data['wallet_address']
    user_lang = lang

    if lang == 'ru':
        return f"""
✨ <b>Ваша информация</b> ✨
━━━━━━━━━━━━━━━━━━
<b>🔑 Кошелек:</b> <code>{user_wallet}</code>
<i>(Нажмите, чтобы скопировать)</i>

<b>💰 Баланс:</b> <b><i>{user_balance}</i></b>

<b>⚠️ Ограничения:</b> {'<b>Заблокирован</b>' if user_status == 'blocked' else 'Вы <b>не ограничены</b>'}

<b>🌐 Язык:</b> {user_lang} 🇷🇺🇨🇳🏴
━━━━━━━━━━━━━━━━━━
"""

    elif lang == 'en':
        return f"""
✨ <b>Your Information</b> ✨
━━━━━━━━━━━━━━━━━━
<b>🔑 Wallet:</b> <code>{user_wallet}</code>
<i>(Click to copy)</i>

<b>💰 Balance:</b> <b><i>{user_balance}</i></b>

<b>⚠️ Restrictions:</b> {'<b>Blocked</b>' if user_status == 'blocked' else 'You are <b>unrestricted</b>'}

<b>🌐 Language:</b> {user_lang} 🇷🇺🇨🇳🏴
━━━━━━━━━━━━━━━━━━
"""

    elif lang == 'cn':
        return f"""
✨ <b>您的信息</b> ✨
━━━━━━━━━━━━━━━━━━
<b>🔑 您的钱包:</b> <code>{user_wallet}</code>
<i>（点击复制）</i>

<b>💰 您的余额:</b> <b><i>{user_balance}</i></b>

<b>⚠️ 限制:</b> {'<b>已阻止</b>' if user_status == 'blocked' else '您<b>未受限制</b>'}

<b>🌐 语言:</b> {user_lang} 🇷🇺🇨🇳🏴
━━━━━━━━━━━━━━━━━━
"""
