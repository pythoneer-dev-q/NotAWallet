from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from app.models import ConstructCheck
from utils import messages
from security import block_database as bdb
import asyncio
import uuid
import app.keyboards as kb
from security.block_database import main_deleteCheck, main_generateCheck, main_searchCheck, main_makeGetCheck, main_searchUser

sendBtnRouter = Router()

@sendBtnRouter.callback_query(F.data.startswith('btn_checks'))
async def main_CheckStarter(call: types.CallbackQuery):
    await call.message.edit_text(text=messages.RuMessages.check_optionalMessage, reply_markup=await kb.main_ProceedCheckBtn())
    await call.answer()
@sendBtnRouter.callback_query(F.data == 'check_starter')
async def main_checkStarter(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите сумму: \n\n<blockquote><b>Подсказка</b>: вы можете создать чек на любую сумму <b>БЕЗ КОМИССИИ</b></blockquote>', reply_markup=await kb.main_CancelCheckBtn())
    await state.set_state(ConstructCheck.amount)
    await call.answer()
@sendBtnRouter.message(ConstructCheck.amount, F.text)
async def main_checkStep2(message: types.Message, state: FSMContext):
    if message.text:
        try:
            amount = float(message.text)
            await state.update_data(amount=amount)
            await state.set_state(ConstructCheck.from_user_id)
            await state.update_data(from_user=message.from_user.id)
            await message.answer(f'Проверьте свои введенные данные:\nСумма: {amount}\nВаш ID: {message.from_user.id}', reply_markup=await kb.main_generateCheckConfirmation(user_id=message.from_user.id, amount=amount))
            await state.set_state(ConstructCheck.confirmation)
        except:
            await message.answer('Неверный ввод суммы. Попробуйте еще раз', reply_markup=await kb.main_CancelCheckBtn())
            await state.set_state(ConstructCheck.amount)

@sendBtnRouter.callback_query(ConstructCheck.confirmation, F.data.startswith('check'))
async def main_generatorCheck(call: types.CallbackQuery, state: FSMContext):
    check, user_id, amount = call.data.split('_')
    if call.from_user.id == int(user_id):
        status_message = await call.message.edit_text(f'Создание чека на {amount} монет...')
        UID, from_wallet, amount = await bdb.main_generateCheck(from_user_id=user_id, amount=amount)
        if UID is not None:
            await status_message.edit_text(f'✅ <b>Чек сгенерирован!</b>\n\nЧтобы получить его, <b><a href="https://t.me/ntwlt_bot?start=chk{UID}">нажмите на ссылку</a></b>\n\n⚠️ <b><i>Никогда</i> не делайте скриншот вашего чека, таким образом вы можете потерять ваши средства!</b>', reply_markup=await kb.main_deleteCheckKb(check_UID=UID))
        else:
            await status_message.edit_text('Не получилось создать чек. <b>Проверьте ваш баланс</b>. Если он больше суммы чека, то обратитесь в поддержку.')


    await call.answer()

@sendBtnRouter.callback_query(F.data == 'check_cancel')
async def main_checkCanceller(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text('Создание отменено. Перейти в меню?', reply_markup=await kb.main_ToMenu())