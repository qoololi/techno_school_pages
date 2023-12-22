from aiogram.fsm.state import StatesGroup, State


class set_group_states(StatesGroup):
    set_subject = State()
    set_teacher = State()