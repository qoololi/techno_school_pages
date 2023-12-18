from aiogram.fsm.state import StatesGroup, State


class set_user_states(StatesGroup):
    set_subject = State()
    set_teacher = State()
    set_date = State()