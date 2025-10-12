from aiogram.fsm.state import StatesGroup, State

class ConstructCheck(StatesGroup):
    from_user_id = State()
    amount = State()
    confirmation = State()

class ConstructInvouce(StatesGroup):
    from_user_id = State()
    amount = State()
    confirmation = State()