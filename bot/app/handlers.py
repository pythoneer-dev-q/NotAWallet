from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
import security.database as main_db
import security.block_database as bdb
import app.keyboards as kb
from asyncio import sleep
from utils import getLang, sort_user_data
from utils.messages import (
    RuMessages, CnMessages, EnMessages
)
router = Router()

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart(deep_link=True))
async def main_starterLinker(message: Message, command: CommandStart):
    args = command.args or ""

    if args.startswith('inv'):
        uid = args.replace('inv', '')
        from_user, amount, UID, status = await bdb.main_searchInvouce(invouce_uid=uid)
        await message.answer(f'Вы точно хотите оплатить данный счет?\nДанные:\n - От: {from_user}\n - Сумма: {amount}\n - ID: {UID}\n - Status: {status}',
                             reply_markup=await kb.main_ProceedInvouce(user_id=message.from_user.id, invouce_uid=UID))
    elif args.startswith('chk'):
        uid = args.replace('inv', '')
        from_user, amount, UID, status = await bdb.main_searchCheck(check_uid=uid)
        await message.answer(f'Вы точно хотите получить данный чек?\nДанные:\n - От: {from_user}\n - Сумма: {amount}\n - ID: {UID}\n - Status: {status}',
                             reply_markup=await kb.main_ProceedCheck(user_id=message.from_user.id, invouce_uid=UID))
    else:
        await message.answer('Неверный идентификатор или ссылка.')

@router.message(CommandStart(deep_link=False))
async def main_startRegister(message: Message):
    user_id = message.from_user.id
    user_data = await main_db.main_searchUser(user_id=user_id)

    if user_data is not None:
        wallet_num = user_data.get('wallet_address', '')
        if user_data['lang'] == 'ru':
            await message.answer(f'{RuMessages.welcome_message}\n\n<b>Ваш кошелек</b>: <code>{wallet_num}</code>', reply_markup=await kb.main_markup(lang=user_data['lang']))
            return
        elif user_data['lang'] == 'en':
            await message.answer(text=f'{EnMessages.welcome_message}\n\n<b>Your wallet</b>: <code>{wallet_num}</code>', reply_markup=await kb.main_markup(lang='en'))
            return
        elif user_data['lang'] == 'cn':
            await message.answer(text=f'{CnMessages.welcome_message}\n\n<b>Your wallet</b>: <code>{wallet_num}</code>', reply_markup=await kb.main_markup(lang='cn'))
            return
    else:
        await message.answer('Please, choose your language below:', reply_markup=await kb.main_registerMarkup())
        return

@router.callback_query(F.data.startswith('lang'))
async def main_completeRegister(call: CallbackQuery):
    _, lang = call.data.split('_')
    user_id = call.from_user.id

    if lang == 'ru':
        progress_message = await call.message.edit_text(text=RuMessages.reg1)
        await sleep(0.5)
        await progress_message.edit_text(text=RuMessages.reg2)
        user_data = await main_db.main_registerUser(user_id=user_id, lang=lang)

        await sleep(0.5)
        await progress_message.edit_text(text=RuMessages.reg3)
        await sleep(0.5)
        if user_data is not None:
            await progress_message.edit_text(text=EnMessages.welcome_message, reply_markup=await kb.main_markup(lang='en'))
            return
        else:
            await progress_message.edit_text(f'an error has occured.')        
            return
    elif lang == 'cn':
        progress_message = await call.message.edit_text(text=CnMessages.reg1)
        await sleep(0.5)
        await progress_message.edit_text(text=CnMessages.reg2)
        user_data = await main_db.main_registerUser(user_id=user_id, lang=lang)

        await sleep(0.5)
        await progress_message.edit_text(text=CnMessages.reg3)
        await sleep(0.5)
        if user_data is not None:
            await progress_message.edit_text(text=EnMessages.welcome_message, reply_markup=await kb.main_markup(lang='en'))
            return
        else:
            await progress_message.edit_text(f'an error has occured.')        
            return
    elif lang == 'en':
        progress_message = await call.message.edit_text(text=EnMessages.reg1)
        await sleep(0.5)
        await progress_message.edit_text(text=EnMessages.reg2)
        user_data = await main_db.main_registerUser(user_id=user_id, lang=lang)

        await sleep(0.5)
        await progress_message.edit_text(text=EnMessages.reg3)
        await sleep(0.5)
        if user_data is not None:
            await progress_message.edit_text(text=EnMessages.welcome_message, reply_markup=await kb.main_markup(lang='en'))
            return
        else:
            await progress_message.edit_text(f'an error has occured.')


@router.callback_query(F.data == 'back_settings')
@router.callback_query(F.data == 'settings')
async def main_settingsLister(call: CallbackQuery):
    user_id = call.from_user.id
    lang = await getLang.main_getLang(user_id=user_id)
    if lang == 'ru':
        await call.message.edit_text(text=RuMessages.settings_message, reply_markup=await kb.settings_markup(lang='ru'))
    elif lang == 'en':
        await call.message.edit_text(text=EnMessages.settings_message, reply_markup=await kb.settings_markup(lang='en'))
    elif lang == 'cn':
        await call.message.edit_text(text=CnMessages.settings_message, reply_markup=await kb.settings_markup(lang='cn'))

@router.callback_query(F.data == 'identy')
async def main_identy(call: CallbackQuery):
    user_id = call.from_user.id
    user_data = await main_db.main_searchUser(user_id=user_id)
    lang = await getLang.main_getLang(user_id=user_id)
    message_text = await sort_user_data.main_sortuserData(lang=lang, user_data=user_data)
    await call.message.edit_text(message_text, reply_markup=await kb.main_backSettings())