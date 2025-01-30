from aiogram import Router, F
from aiogram.fsm.state import any_state

from PyCharmProject.telegram_bot.handlers.user_u_i.connection_to_parent import parse_callback_from_request_to_add_parent
from PyCharmProject.telegram_bot.handlers.user_u_i.user_u_i import user_cabinet, user_groups, user_u_i_back_to_menu
from PyCharmProject.telegram_bot.keyboards.callback_factories.add_parent_callback_data import AddParentCallbackData


def register_user_u_i_router(user_router: Router):
    user_router.callback_query.register(user_u_i_back_to_menu, F.data == 'user_u_i_start')
    user_router.callback_query.register(user_cabinet, F.data == 'user_cabinet')
    user_router.callback_query.register(user_groups, F.data == 'user_u_i_my_groups')
    user_router.callback_query.register(parse_callback_from_request_to_add_parent, AddParentCallbackData.filter())
