from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from PyCharmProject.telegram_bot.keyboards.callback_factories.add_parent_callback_data import AddParentCallbackData
from PyCharmProject.telegram_bot.keyboards.callback_factories.group_callback_data import GroupCallbackData
from PyCharmProject.telegram_bot.maps.subjects import subjects_names


def user_u_i_start_kb():
    markup = InlineKeyboardBuilder().add(
        types.InlineKeyboardButton(text="Мой личный кабинет",
                                   callback_data='user_cabinet'))
    markup.add(
        types.InlineKeyboardButton(text="О нас", web_app=types.WebAppInfo(
            url="https://technoschool-workspace.ru/visit.html"))
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)

def user_u_i_cabinet_kb():
    markup = InlineKeyboardBuilder().add(
        types.InlineKeyboardButton(text="Мои группы.", callback_data='user_u_i_my_groups'))
    markup.add(
        types.InlineKeyboardButton(text="Назад.", callback_data='user_u_i_start')
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)

def user_u_i_groups_kb(groups):
    markup = InlineKeyboardBuilder()
    for group in groups:
        markup.add(
            types.InlineKeyboardButton(text=subjects_names[group[0]], callback_data=GroupCallbackData(group_id=group[1], tg_chat_id=group[2]).pack())
        )
    markup.add(types.InlineKeyboardButton(text="Назад.", callback_data='user_cabinet'))
    markup.adjust(1)
    return markup.as_markup(row_width=1)

def user_add_parent_kb(parent_tg_user_id:int):
    markup = InlineKeyboardBuilder().add(
        types.InlineKeyboardButton(text="✔️Подтвердить",
                                   callback_data=AddParentCallbackData(parent_tg_user_id=parent_tg_user_id, accept_flag=True).pack()),
        types.InlineKeyboardButton(text="❌Отменить",
                                   callback_data=AddParentCallbackData(parent_tg_user_id=parent_tg_user_id, accept_flag=False).pack())
    )
    markup.adjust(2)
    return markup.as_markup(row_width=1)