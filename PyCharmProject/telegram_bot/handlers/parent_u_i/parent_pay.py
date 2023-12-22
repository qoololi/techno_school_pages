from aiogram import types
from aiogram.fsm.context import FSMContext

from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_callback_data import ParentChildChooseBundles, \
    ParentChildChooseSubscribe
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_pay_callback_data import \
    ParentBuyCourseCallbackData
from PyCharmProject.telegram_bot.keyboards.parent_inline_kbs import parent_u_i_pay_start_kb, parent_u_i_pay_bundles_kb, \
    parent_u_i_pay_course_select_term_kb
from PyCharmProject.telegram_bot.texts.parent_texts import parent_u_i_choose_subscribe_name_text, \
    parent_u_i_choose_bundle_text, parent_u_i_pay_course_select_term_text


async def parent_u_i_pay_selector(query: types.CallbackQuery, callback_data: ParentBuyCourseCallbackData):
    await query.message.edit_caption(
        caption=parent_u_i_choose_subscribe_name_text(tg_child_id=callback_data.child_tg_user_id),
        reply_markup=parent_u_i_pay_start_kb(callback_data.child_tg_user_id))


async def parent_u_i_pay_bundles(query: types.CallbackQuery, callback_data: ParentChildChooseBundles):
    await query.message.edit_caption(caption=parent_u_i_choose_bundle_text(tg_child_id=callback_data.tg_child_id),
                                     reply_markup=parent_u_i_pay_bundles_kb(callback_data))

async def parent_u_i_pay_course_select_term(query: types.CallbackQuery, callback_data: ParentChildChooseSubscribe):
    await query.message.edit_caption(caption=parent_u_i_pay_course_select_term_text(data=callback_data), reply_markup=parent_u_i_pay_course_select_term_kb(data=callback_data))