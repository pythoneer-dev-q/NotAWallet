from aiogram import Router, F, types
import asyncio
import uuid
import app.keyboards as kb
from security.block_database import main_deleteCheck, main_generateCheck, main_searchCheck, main_makeGetCheck

router_inlineChecks = Router()


@router_inlineChecks.inline_query(F.query.startswith("chk "))
async def main_InlineInvouce(query: types.InlineQuery):
    content_text = query.query.replace("chk ", "").strip() or "0"
    inline_id = str(uuid.uuid4())
    try:
        content_text = int(content_text)
        result = types.InlineQueryResultArticle(
            id=inline_id,
            title=f"⚡️ Создать чек на {content_text} монет",
            input_message_content=types.InputTextMessageContent(
                message_text=f"Нажмите на кнопку, чтобы создать чек на {content_text} монет..."
            ),
            reply_markup=await kb.proceed_check(amount=content_text)
        )
        await query.answer(results=[result], cache_time=1)
    except Exception:
        result = types.InlineQueryResultArticle(
            id=inline_id,
            title=f"Сумма должа быть числом!",
            input_message_content=types.InputTextMessageContent(
                message_text=f"❌ Нельзя создать такой чек. Возможно, у тебя недостаточно средств или сумма некорректна"
            ))
        await query.answer(results=[result], cache_time=0)


@router_inlineChecks.callback_query(F.data.startswith("start_check:"))
async def start_check(call: types.CallbackQuery):
    amount = call.data.split(":")[1]
    user_id = call.from_user.id
    tx_UID, from_user, amount = await main_generateCheck(from_user_id=user_id, amount=amount)
    if call.message:
        if tx_UID is None:
            await call.message.edit_text(text=f"Недостаточно средств на балансе.")
            await call.answer('Недостаточно средств. Попробуйте пополнить.')
            return
        await call.message.edit_text(f"⏳ Создаём Чек на {amount} монет...")
        await asyncio.sleep(1)
        await call.message.edit_text(
            text=f"✅ Чек на {amount} монет готов!\n<b>Данные</b>:\n - От: <b>{from_user}</b>\n - UID: <code>{tx_UID}</code>\nНажмите кнопку для получения.",
            reply_markup=await kb.main_getCheck(check_amount=amount, check_uid=tx_UID)
        )
    elif call.inline_message_id:
        if tx_UID is None:
            await call.bot.edit_message_text(
                text=f"Недостаточно средств на балансе.",
                inline_message_id=call.inline_message_id
            )
            await call.answer('Недостаточно средств. Попробуйте пополнить.')
            return
        inline_id = call.inline_message_id
        await call.bot.edit_message_text(inline_message_id=inline_id,
                                         text=f"⏳ Создаём Чек на {amount} монет...")
        await asyncio.sleep(2)
        await call.bot.edit_message_text(inline_message_id=inline_id,
                                         text=f"✅ Чек на {amount} монет готов!\n<b>Данные</b>:\n - От: <b>{from_user}</b>\n - UID: <code>{tx_UID}</code>\nНажмите кнопку для получения.",
                                         reply_markup=await kb.main_getCheck(check_amount=amount, check_uid=tx_UID))
    await call.answer()


@router_inlineChecks.callback_query(F.data.startswith("delete:check:"))
async def cancel_invoice(call: types.CallbackQuery):
    uid = call.data.split(":")[2]
    #amount, wallet_from, check_uid, clicked_user_id
    amount, wallet_from, check_uid, from_user = await main_deleteCheck(clicked_user_id=call.from_user.id, invouce_UID=uid)
    if (amount is not None) and call.message:
        await call.message.edit_text(
            f"❌ Чек {uid} отменен!\nВы больше не сможете получить его.\nДанные:\n - <b>От кого: {from_user}</b>\n - <b>Сумма: {amount}</b>", reply_markup=await kb.main_deletedCheckKb(invouce_uid=uid)
        )
    elif (amount is not None) and call.inline_message_id:
        await call.bot.edit_message_text(inline_message_id=call.inline_message_id,
                                         text=f"❌ Чек {uid} отменен!\nВы больше не сможете получить его.\nДанные:\n - <b>От кого: {from_user}</b>\n - <b>Сумма: {amount}</b>", reply_markup=await kb.main_deletedCheckKb(invouce_uid=uid))
    else:
        await call.answer('Эта кнопка не для тебя..')
    await call.answer("Чек отменён", show_alert=False)


@router_inlineChecks.callback_query(F.data.startswith('chk'))
async def main_checkProceeder(call: types.CallbackQuery):
    check_type, user_receiver, UID = call.data.split(':')
    from_user, amount, UID, status = await main_searchCheck(check_uid=UID)
    status_message = await call.message.edit_text(f'Пытаюсь получить чек на {amount} от <code>{from_user}</code>...')
    #                return from_user, user, after_balance, UID, status
    from_user, recipient_user, after_balance, UID, status = await main_makeGetCheck(user_recipient=call.from_user.id, check_uid=UID)
    if (status != 1) and from_user is not None:
        await status_message.edit_text(f"""
✅ <b>Чек {check_type}v1 №{UID} успешно получен Вами</b>
Данные:<blockquote>
<code>Получатель: {call.from_user.id}
Сумма: {amount}
UID: {UID}</code></blockquote>
Спасибо, что используете NotAWallet""")
        await call.bot.send_message(chat_id=from_user, text=f'✅ Ваш чек <code>{UID}</code> был получен пользователем {recipient_user}')

    else:
        await status_message.edit_text('Этот чек уже активирован.')
