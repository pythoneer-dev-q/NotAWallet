from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from app.models import ConstructInvouce
from utils import messages
from security import block_database as bdb
import asyncio
import uuid
import app.keyboards as kb
from security.block_database import main_generateInvouce, main_deleteInvouce, main_searchUser

invBtnRoter = Router()

@invBtnRoter.callback_query(F.data == 'btn_invouces')
async def main_InvouceStarter(call: types.CallbackQuery):
    await call.message.edit_text(text=messages.RuMessages.inv_optionalMessage, reply_markup=await kb.main_ProceedInvouceBtn())


@invBtnRoter.callback_query(F.data == 'invouce_starter')
async def main_InvouceStep2(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите сумму: \n\n<blockquote><b>Подсказка</b>: вы можете создать счет на любую сумму <b>БЕЗ КОМИССИИ</b></blockquote>', reply_markup=await kb.main_CancelInvouceBtn())
    await state.set_state(ConstructInvouce.amount)
    await call.answer()

@invBtnRoter.message(ConstructInvouce.amount, F.text)
async def main_AmountCheckInvouce(message: types.Message, state: FSMContext):
        if message.text:
            try:
                amount = float(message.text)
                await state.update_data(amount=amount)
                await state.set_state(ConstructInvouce.from_user_id)
                await state.update_data(from_user=message.from_user.id)
                await message.answer(f'Проверьте свои введенные данные:\nСумма: {amount}\nВаш ID: {message.from_user.id}', reply_markup=await kb.main_generateInvouceConfirmation(user_id=message.from_user.id, amount=amount))
                await state.set_state(ConstructInvouce.confirmation)
            except:
                await message.answer('Неверный ввод суммы. Попробуйте еще раз', reply_markup=await kb.main_CancelInvouceBtn())
                await state.set_state(ConstructInvouce.amount)
        else:
             await message.answer('что это?')

@invBtnRoter.callback_query(ConstructInvouce.confirmation, F.data.startswith('invouce'))
async def generator(call: types.CallbackQuery, state: FSMContext):
    check, user_id, amount = call.data.split('_')
    if call.from_user.id == int(user_id):
        status_message = await call.message.edit_text(f'Создание счета на {amount} монет...')
        UID, from_user = await bdb.main_generateInvouce(from_user_id=user_id, amount=amount)
        if UID is not None:
            await status_message.edit_text(f'✅ <b>Счет сгенерирован!</b>\n\nЧтобы оплатить его, <b><a href="https://t.me/ntwlt_bot?start=inv{UID}">нажмите на ссылку</a></b>\n\n⚠️ <b><i>Счет одноразовый.</i>После того, как вы его оплатите, он сразу станет недоступен для оплаты другим.</b>', reply_markup=await kb.main_deleteInvouceKb(invouce_UID=UID))
        else:
            await status_message.edit_text('Не получилось создать счет. <b>Проверьте вашу регистрацию</b>.')


    await call.answer()
