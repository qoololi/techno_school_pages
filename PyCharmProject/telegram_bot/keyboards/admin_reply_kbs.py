from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from PyCharmProject.telegram_bot.MVC.controllers.teacher_controller import teacher_controller
from PyCharmProject.telegram_bot.maps.subjects import subjects_names


def subjects_kb():
    markup = ReplyKeyboardBuilder()
    for name in list(subjects_names.keys()):
        markup.button(text=name)
    markup.button(text="Отмена")
    markup.adjust(3)
    return markup.as_markup(resize_keyboard=True)

def teachers_by_subject_kb(subject_name):
    teachers = teacher_controller.get_short_teachers_names_by_subject(subject_name)
    markup = ReplyKeyboardBuilder()
    for teacher in teachers:
        markup.button(text=teacher)
    markup.button(text="Отмена")
    markup.adjust(3)
    return markup.as_markup(resize_keyboard=True)