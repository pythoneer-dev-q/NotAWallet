from aiogram import Router, F, types
import hashlib
import asyncio
import app.keyboards as kb
from security import block_database as bdb
from security.block_database import main_generateInvouce, main_deleteInvouce
router_inlineInvouce = Router()


@router_inlineInvouce.inline_query(F.query.startswith("inv "))
async def main_InlineInvouce(query: types.InlineQuery):
    content_text = query.query.replace("inv ", "").strip() or "0"
    inline_id = hashlib.md5(content_text.encode()).hexdigest()
    try:
        content_text = int(content_text)
        result = types.InlineQueryResultArticle(
            id=inline_id,
            title=f"💰 Создать счёт на {content_text} монет",
            input_message_content=types.InputTextMessageContent(
                message_text=f"Нажмите на кнопку, чтобы создать счет на {content_text} монет..."
            ),
            reply_markup=await kb.proceed_invouce(amount=content_text))

        await query.answer(results=[result], cache_time=1)
    except Exception as e:
        result = types.InlineQueryResultArticle(
            id=inline_id,
            title=f"Сумма должа быть числом!",
            input_message_content=types.InputTextMessageContent(
                message_text=f"❌ Нельзя создать такой счет."
            ))
        await query.answer(results=[result], cache_time=0)




@router_inlineInvouce.callback_query(F.data.startswith("start_invoice:"))
async def start_invoice(call: types.CallbackQuery):
    amount = call.data.split(":")[1]
    user_id = call.from_user.id

    uid, from_user = await main_generateInvouce(from_user_id=user_id, amount=amount)
    # если обычное сообщение
    if call.message:
        await call.message.edit_text(f"⏳ Создаём счёт на {amount} монет...")
        await asyncio.sleep(0/7)
        await call.message.edit_text(
            text=f"✅ Счёт на {amount} монет готов!\n<b>Данные</b>:\n - От: {from_user}\n - UID: <code>{uid}</code>\nНажмите кнопку для оплаты или отмены.",
            reply_markup=await kb.main_payInvouce(invouce_amount=amount, invouce_uid=uid)
        )
    # если inline-сообщение (в чужом чате)
    elif call.inline_message_id:
        inline_id = call.inline_message_id
        await call.bot.edit_message_text(inline_message_id=inline_id,
                                       text=f"⏳ Создаём счёт на {amount} монет...")
        await asyncio.sleep(2)
        await call.bot.edit_message_text(inline_message_id=inline_id,
                                       text=f"✅ Счёт на {amount} монет готов!\n<b>Данные</b>:\n - От: {from_user}\n - UID: <code>{uid}</code>\nНажмите кнопку для оплаты или отмены.",
                                       reply_markup=await kb.main_payInvouce(invouce_amount=amount, invouce_uid=uid))

    await call.answer()


@router_inlineInvouce.callback_query(F.data.startswith("delete:invouce:"))
async def cancel_invoice(call: types.CallbackQuery):
    uid = call.data.split(":")[2]
    status, from_user, amount  = await main_deleteInvouce(clicked_user_id=call.from_user.id, invouce_UID=uid)
    if (status is not None) and call.message:
        await call.message.edit_text(f"❌ Счёт {uid} отменен!\nВы больше не сможете оплатить его.\nДанные:\n - <b>От кого: {from_user}</b>\n - <b>Сумма: {amount}</b>", reply_markup=await kb.main_deletedInvouceKb(invouce_uid=uid))
    elif (status is not None) and call.inline_message_id:
        await call.bot.edit_message_text(inline_message_id=call.inline_message_id,
                                       text=f"❌ Счёт {uid} отменен!\nВы больше не сможете оплатить его.\nДанные:\n - <b>От кого: {from_user}</b>\n - <b>Сумма: {amount}</b>", reply_markup=await kb.main_deletedInvouceKb(invouce_uid=uid))
    else:
        await call.answer('Эта кнопка не для тебя..')
    await call.answer("Счёт отменён", show_alert=False)


# оплата счета 
@router_inlineInvouce.callback_query(F.data.startswith('inv:'))
async def main_invouceDecr(call: types.CallbackQuery):
    #from_user, amount, UID, status
    invtype, pay_user, invouce_uid = call.data.split(':')
    from_user, amount, UID, status = await bdb.main_searchInvouce(invouce_uid=invouce_uid)
    status_message = await call.message.edit_text(f'Попытка списать {amount} по счету <b>#{UID}</b>...')
    from_user_id, from_user_balanceAfter, amount, invouce_uid = await bdb.main_makePayUser(user_id=pay_user, invouce_uid=invouce_uid)
    # return from_user_id, from_user_idBalanceAfter, amount, invouce_uid
    if from_user_id is not None:
        user_payeer = call.from_user.id

        await status_message.edit_text(f"""
✅ <b>Счет {invtype}v1 №{invouce_uid} Успешно оплачен пользователем {user_payeer}</b>
Данные:<blockquote>
<code>Получатель: {from_user_id}
Баланс получателя после: {from_user_balanceAfter}
Сумма: {amount}
UID: {invouce_uid}</code></blockquote>
Спасибо, что используете NotAWallet""")
        print(from_user_id)
        await call.bot.send_message(chat_id=from_user_id, text=f"""✅ <b>Ваш счет был оплачен пользователем {call.from_user.id}</b>\nДанные:
<blockquote><code>Получатель: {from_user_id}
Баланс получателя после: {from_user_balanceAfter}
Сумма: {amount}
UID: {invouce_uid}</code></blockquote>
Спасибо, что используете NotAWallet""")
        

    