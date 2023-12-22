from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def parent_u_i_add_child_kb():
    markup = ReplyKeyboardBuilder()
    markup.add(
        types.KeyboardButton(text="Привязка ребенка",
                                   web_app=types.WebAppInfo(
                                       url="https://technoschool-workspace.ru/add_child.html")))
    markup.button(text="Отмена")
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)