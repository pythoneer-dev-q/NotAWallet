from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from security import database as db
from config import bot_config
from app import keyboards as kb
adminrouter = Router()

class NewsMessage(StatesGroup):
    title = State()
    text = State()
    confirmation = State()


@adminrouter.message(F.text == '/new_news')
async def main_NewNewser(message: Message, state: FSMContext):
    if message.from_user.id in bot_config.admin_user:
        await state.set_state(NewsMessage.title)
        await message.answer('Введите заголовок новости..')
    else:
        await message.answer('доступ закрыт.')

@adminrouter.message(NewsMessage.title)
async def main_NewsUpdater(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(NewsMessage.text)
    await message.answer('введите текст новости')

@adminrouter.message(NewsMessage.text)
async def main_proceed(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await message.answer(f'Проверьте текст и заголовок: \n\n{data['title']}\n\n{data['text']}', reply_markup=await kb.main_adminPublish())
    await state.set_state(NewsMessage.confirmation)

@adminrouter.callback_query(NewsMessage.confirmation, F.data == 'publish')
async def main_publisher(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    get_data = await db.main_WriteNews(user_id=call.from_user.id, text=data['text'], title=data['title'])
    if get_data is not None:
        await call.message.edit_text(f'Новость опубликована. Время публикации {get_data}')
    else:
        await call.answer('ошибка')
    await call.answer('Завершил работу')
    await state.clear()