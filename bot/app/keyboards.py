from aiogram.types import InlineKeyboardButton as kb_btn
from aiogram.types import InlineKeyboardMarkup as kb_mrk
from config.main_cofig import server_URI

async def main_registerMarkup():
            keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='🇷🇺 RU', callback_data='lang_ru'), 
            kb_btn(text='🇨🇳 CN', callback_data='blocked'),
            kb_btn(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN', callback_data='blocked')]])
            return keyboard

async def main_markup(lang: str):
    if lang == 'ru':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='📄 Чеки', callback_data='btn_checks'), 
            kb_btn(text='💰 Счета', callback_data='btn_invouces')],
            [kb_btn(text='📲 Перевод', callback_data='blocked')],
            [kb_btn(text='⚙️ Настройки', callback_data='settings'),
             kb_btn(text='❔ Помощь', callback_data='help')],
            [kb_btn(text='📡 API', callback_data='api'),
             kb_btn(text='📰 Новости', callback_data='call_news')],
            
            ])
        return keyboard
    elif lang == 'en':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='📄 Checks', callback_data='btn_checks'), 
            kb_btn(text='💰 Invouces', callback_data='btn_invouces')],
            [kb_btn(text='⚙️ Settings', callback_data='settings'),
             kb_btn(text='❔ Help', callback_data='help')],
            [kb_btn(text='📡 API', callback_data='api')]
            ])
        return keyboard
    elif lang == 'cn':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='📄 检查', callback_data='btn_checks'), 
            kb_btn(text='💰 账户', callback_data='btn_invouces')],
            [kb_btn(text='⚙️ 设置', callback_data='settings'),
             kb_btn(text='❔ 帮助', callback_data='help')],
            [kb_btn(text='📡 API', callback_data='api')]
            ])
        return keyboard
async def settings_markup(lang: str):
    if lang == 'ru':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='👤 Личность', callback_data='identy'), 
            kb_btn(text='🛡 Ваши данные', callback_data='personal_data')],
            [kb_btn(text='⚙️ Язык/Lang', callback_data='blocked')],
            [
         kb_btn(text='⬱', callback_data='back_menu')
    ]
            ])
        return keyboard
    elif lang == 'en':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='👤 Person', callback_data='identy'), 
            kb_btn(text='🛡 Personal info', callback_data='personal_data')],
            [kb_btn(text='⚙️ Язык/Lang', callback_data='blocked')],
            [
         kb_btn(text='⬱', callback_data='back_menu')
    ]
            ])
        return keyboard
    elif lang == 'cn':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='👤 性格 ', callback_data='identy'), 
            kb_btn(text='🛡 你的数据', callback_data='personal_data')],
            [kb_btn(text='⚙️ Язык/Lang', callback_data='lang_reset')],
            [
         kb_btn(text='⬱', callback_data='back_menu')
    ]
            ])
        return keyboard
async def main_backSettings():
    keyboard = kb_mrk(inline_keyboard=[[
         kb_btn(text='⬱', callback_data='back_settings')
    ]])
    return keyboard

async def main_payInvouce(invouce_amount: float, invouce_uid: str):
    keyboard = kb_mrk(inline_keyboard=[[
         kb_btn(text=f'💳 Оплатить {invouce_amount}', url=f'https://t.me/ntwlt_bot?start=inv{invouce_uid}'),
         kb_btn(text='❌ Отказаться', callback_data=f'delete:invouce:{invouce_uid}')
    ],
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/invoice/{invouce_uid}')]])
    return keyboard

async def proceed_invouce(amount: int, user_id):
    keyboard = kb_mrk(inline_keyboard=[[kb_btn(
                    text="Начать создание",
                    callback_data=f"start_invoice:{amount}:{user_id}"
                )]
            ]
        )
    return keyboard

async def proceed_check(amount: int, user_id):
    keyboard = kb_mrk(inline_keyboard=[[kb_btn(
                    text="Создать чек",
                    callback_data=f"start_check:{amount}:{user_id}"
                )]
            ]
        )
    return keyboard
async def main_getCheck(check_amount: float, check_uid: str):
    keyboard = kb_mrk(inline_keyboard=[[
         kb_btn(text=f'💳 Получить {check_amount}', url=f'https://t.me/ntwlt_bot?start=chk{check_uid}'),
         kb_btn(text='❌ Отказаться', callback_data=f'delete:check:{check_uid}')],
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/check/{check_uid}')]])
    return keyboard

async def main_deletedCheckKb(check_uid: str):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/check/{check_uid}')]])
    return keyboard

async def main_deletedInvouceKb(invouce_uid: str):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/invoice/{invouce_uid}')]])
    return keyboard
async def main_ProceedInvouce(invouce_uid: str, user_id: int):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='⚡️ Списать со счета', callback_data = f'inv:{user_id}:{invouce_uid}')],
         [kb_btn(text='❌ Отказаться', callback_data='back_menu')]])
    return keyboard
async def main_ProceedInvouceBtn():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='Создать счет', callback_data = f'invouce_starter')],
         [kb_btn(text='💬 Создать из чата', switch_inline_query='inv ')],
         [kb_btn(text='⬱', callback_data='back_menu')]])
    return keyboard
async def main_CancelInvouceBtn():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❌ Отменить создание', callback_data = f'invouce_cancel')]])
    return keyboard

async def main_generateInvouceConfirmation(user_id: int, amount: float):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='✅ Все верно, создать счет', callback_data = f'invouce_{user_id}_{amount}')],
         [kb_btn(text='❌ Отменить создание', callback_data = f'invouce_cancel')]])
    return keyboard

async def main_deleteInvouceKb(invouce_UID: str):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❌ Удалить счет', callback_data = f'delete:invouce:{invouce_UID}')],
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/invoice/{invouce_UID}')]])
    return keyboard



async def main_ProceedCheck(invouce_uid: str, user_id: int):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='⚡️ Получить', callback_data = f'chk:{user_id}:{invouce_uid}')],
         [kb_btn(text='❌ Отказаться', callback_data='back_menu')]])
    return keyboard

async def main_ProceedCheckBtn():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='Создать чек', callback_data = f'check_starter')],
         [kb_btn(text='💬 Создать из чата', switch_inline_query='chk ')],
         [kb_btn(text='⬱', callback_data='back_menu')]])
    return keyboard
async def main_generateCheckConfirmation(user_id: int, amount: float):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='✅ Все верно, создать чек', callback_data = f'check_{user_id}_{amount}')],
         [kb_btn(text='❌ Отменить создание', callback_data = f'check_cancel')]])
    return keyboard
async def main_CancelCheckBtn():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❌ Отменить создание', callback_data = f'check_cancel')]])
    return keyboard

async def main_deleteCheckKb(check_UID: str):
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='❌ Удалить чек', callback_data = f'delete:check:{check_UID}')],
         [kb_btn(text='❔ Посмотреть в Explorer', url=f'{server_URI}?call=/server/check/{check_UID}')]])
    return keyboard

async def main_ToMenu():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='⬱ В меню', callback_data = f'back_menu')]])
    return keyboard


async def main_adminPublish():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='Опубликовать новость', callback_data = f'publish')],
         [kb_btn(text='Отмена', callback_data='cancel_publishing')]])
    return keyboard

async def main_showNewsKb(news_titles: list[str]):
    inline_keyboard = []

    for title in news_titles:
        inline_keyboard.append([kb_btn(text=title, callback_data=f'news_title:{title}')])

    inline_keyboard.append([kb_btn(text='⬱', callback_data='back_menu')])
    keyboard = kb_mrk(inline_keyboard=inline_keyboard)

    return keyboard or None

async def main_backNews():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='⬱ К новостям', callback_data = f'back_news')]])
    return keyboard

async def main_APiKB(user_id: int):
    keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='🔑 Получить ключ', callback_data=f'get_key:{user_id}'),
            kb_btn(text='❌ Сбросить ключ', callback_data=f'blocked')],
            [kb_btn(text='📃 Документация (OpenAPI)', url='https://notawallet.sbs/docs')],
            [kb_btn(text='🕸 Ошибки (Сервер)', url='https://notawallet.sbs/errs')],
         [kb_btn(text='⬱', callback_data = f'back_menu')]])
    return keyboard

async def main_backaApi():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='⬱ К API', callback_data = f'back_api')]])
    return keyboard

async def main_Help():
    keyboard = kb_mrk(inline_keyboard=[
         [kb_btn(text='🆘 Написать в поддержку', url= f'https://t.me/notawalletsupport')],
         [kb_btn(text='⬱', callback_data = f'back_menu')]
         ])
    return keyboard