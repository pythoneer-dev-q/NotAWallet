from aiogram.types import InlineKeyboardButton as kb_btn
from aiogram.types import InlineKeyboardMarkup as kb_mrk

async def main_registerMarkup():
            keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='🇷🇺 RU', callback_data='lang_ru'), 
            kb_btn(text='🇨🇳 CN', callback_data='lang_cn'),
            kb_btn(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN', callback_data='lang_en')]])
            return keyboard

async def main_markup(lang: str):
    if lang == 'ru':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='📄 Чеки', callback_data='btn_checks'), 
            kb_btn(text='💰 Счета', callback_data='btn_invouces')],
            [kb_btn(text='⚙️ Настройки', callback_data='settings'),
             kb_btn(text='❔ Помощь', callback_data='help')],
            [kb_btn(text='📡 API', callback_data='api')]
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
            [kb_btn(text='⚙️ Язык/Lang', callback_data='lang_reset')],
            [
         kb_btn(text='<<', callback_data='back_menu')
    ]
            ])
        return keyboard
    elif lang == 'en':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='👤 Person', callback_data='identy'), 
            kb_btn(text='🛡 Personal info', callback_data='personal_data')],
            [kb_btn(text='⚙️ Язык/Lang', callback_data='lang_reset')],
            [
         kb_btn(text='<<', callback_data='back_menu')
    ]
            ])
        return keyboard
    elif lang == 'cn':
        keyboard = kb_mrk(inline_keyboard=[[
            kb_btn(text='👤 性格 ', callback_data='identy'), 
            kb_btn(text='🛡 你的数据', callback_data='personal_data')],
            [kb_btn(text='⚙️ Язык/Lang', callback_data='lang_reset')],
            [
         kb_btn(text='<<', callback_data='back_menu')
    ]
            ])
        return keyboard
async def main_backSettings():
    keyboard = kb_mrk(inline_keyboard=[[
         kb_btn(text='<<', callback_data='back_settings')
    ]])
    return keyboard

async def main_payInvouce(invouce_amount: float, invouce_uid: str):
    keyboard = kb_mrk(inline_keyboard=[[
         kb_btn(text=f'💳 Оплатить {invouce_amount}', url=f'https://t.me/ntwlt_bot?start=inv{invouce_uid}'),
         kb_btn(text='❌ Отказаться', callback_data=f'delete:invouce:{invouce_uid}')
    ]])
    return keyboard

async def proceed_invouce(amount: int):
    keyboard = kb_mrk(inline_keyboard=[[kb_btn(
                    text="Начать создание",
                    callback_data=f"start_invoice:{amount}"
                )]
            ]
        )
    return keyboard