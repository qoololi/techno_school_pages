from aiogram import types

import PyCharmProject.telegram_bot.texts.buttons_texts.reply_buttons_texts
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_buttons(teacher_ui_flag: bool, admin_ui_flag: bool):
    markup = ReplyKeyboardBuilder().add(
        types.KeyboardButton(
            text=PyCharmProject.telegram_bot.texts.buttons_texts.reply_buttons_texts.choose_student_ui))
    if teacher_ui_flag:
        markup.add(types.KeyboardButton(
            text=PyCharmProject.telegram_bot.texts.buttons_texts.reply_buttons_texts.choose_teacher_ui))
    if admin_ui_flag:
        markup.add(types.KeyboardButton(
            text=PyCharmProject.telegram_bot.texts.buttons_texts.reply_buttons_texts.choose_admin_ui))
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)


def register_button():
    markup = ReplyKeyboardBuilder().add(

        types.KeyboardButton(text="Регистрация",
                                   web_app=types.WebAppInfo(
                                       url="https://technoschool-workspace.ru/register_page.html")))
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)
