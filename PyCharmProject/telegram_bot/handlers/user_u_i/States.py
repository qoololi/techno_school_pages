from aiogram.fsm.state import StatesGroup, State


class user_u_i_states(StatesGroup):
    user_menu = State()
    user_personal_cabinet = State()
    user_groups = State()