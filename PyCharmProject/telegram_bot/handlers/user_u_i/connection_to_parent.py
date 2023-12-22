from aiogram import types

from PyCharmProject.telegram_bot.MVC.controllers.parent_controller import parent_controller
from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.keyboards.callback_factories.add_parent_callback_data import AddParentCallbackData
from PyCharmProject.telegram_bot.keyboards.user_inline_kbs import user_add_parent_kb
from PyCharmProject.telegram_bot.texts.user_u_i_texts import request_to_add_parent_text, user_u_i_cancel_parent, \
    user_u_i_accept_parent


async def send_request_to_add_parent(parent_tg_user_id: int, tg_user_id: int):
    from PyCharmProject.telegram_bot.bot import bot
    names = user_controller.get_user_name(tg_user_id=parent_tg_user_id)
    await bot.send_message(chat_id=tg_user_id, text=request_to_add_parent_text(
        last_name=names[0], first_name=names[1], second_name=names[2]
    ), reply_markup=user_add_parent_kb(parent_tg_user_id))

async def parse_callback_from_request_to_add_parent(query:types.CallbackQuery, callback_data: AddParentCallbackData):
    from PyCharmProject.telegram_bot.bot import bot
    if callback_data.accept_flag:
        await query.answer(text="✔️accepted")
        parent_controller.add_child(child_tg_user_id=query.from_user.id, parent_tg_user_id=callback_data.parent_tg_user_id)
        await bot.send_message(chat_id=callback_data.parent_tg_user_id, text=user_u_i_accept_parent(query.from_user.id))
    else:
        await bot.send_message(chat_id=callback_data.parent_tg_user_id, text=user_u_i_cancel_parent(query.from_user.id))

    await query.message.delete()