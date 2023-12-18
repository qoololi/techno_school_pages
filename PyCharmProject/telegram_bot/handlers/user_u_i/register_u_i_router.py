from aiogram import Router, F
from aiogram.fsm.state import any_state

from PyCharmProject.telegram_bot.handlers.user_u_i.States import user_u_i_states
from PyCharmProject.telegram_bot.handlers.user_u_i.user_u_i import user_u_i_start, user_cabinet, user_groups, \
    user_u_i_back_to_menu


def register_u_i_router(user_router: Router):
    user_router.callback_query.register(user_u_i_back_to_menu, F.data == 'user_u_i_start', user_u_i_states.user_personal_cabinet)
    user_router.callback_query.register(user_cabinet, F.data == 'user_cabinet', user_u_i_states.user_menu)
    user_router.callback_query.register(user_groups, F.data == 'user_u_i_my_groups', user_u_i_states.user_personal_cabinet)
