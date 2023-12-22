from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.state import any_state

from PyCharmProject.telegram_bot.handlers.parent_u_i.parent_add_child import parent_add_child, parent_add_child_cancel, \
    parent_add_child_catching_data
from PyCharmProject.telegram_bot.handlers.parent_u_i.parent_pay import parent_u_i_pay_selector, parent_u_i_pay_bundles, \
    parent_u_i_pay_course_select_term
from PyCharmProject.telegram_bot.handlers.parent_u_i.parent_u_i import parent_u_i_back_to_menu, parent_cabinet, \
    parent_children, parent_u_i_child
from PyCharmProject.telegram_bot.keyboards.callback_factories.child_callback_data import ChildCallbackData
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_callback_data import ParentChildChooseBundles, \
    ParentChildChooseSubscribe
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_pay_callback_data import \
    ParentBuyCourseCallbackData
from PyCharmProject.telegram_bot.states.parent_states import parent_u_i_adding_child


def register_parent_u_i_router(parent_router: Router):
    parent_router.callback_query.register(parent_u_i_back_to_menu, F.data == 'parent_u_i_start')
    parent_router.callback_query.register(parent_cabinet, F.data == 'parent_cabinet')
    parent_router.callback_query.register(parent_children, F.data == 'parent_u_i_my_children')
    parent_router.callback_query.register(parent_add_child, F.data == 'parent_u_i_add_child')
    parent_router.callback_query.register(parent_u_i_child, ChildCallbackData.filter())
    parent_router.message.register(parent_add_child_cancel, F.text == 'Отмена',
                                   parent_u_i_adding_child.waiting_webapp_data)
    parent_router.message.register(parent_add_child_catching_data, F.content_type.in_(ContentType.WEB_APP_DATA),
                                   parent_u_i_adding_child.waiting_webapp_data)
    parent_router.callback_query.register(parent_u_i_pay_selector, ParentBuyCourseCallbackData.filter())
    parent_router.callback_query.register(parent_u_i_pay_bundles, ParentChildChooseBundles.filter())
    parent_router.callback_query.register(parent_u_i_pay_course_select_term, ParentChildChooseSubscribe.filter())