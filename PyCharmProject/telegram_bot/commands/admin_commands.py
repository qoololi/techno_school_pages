from aiogram import types
from aiogram.fsm.context import FSMContext

from PyCharmProject.telegram_bot.MVC.controllers.admin_controller import admin_controller
from PyCharmProject.telegram_bot.MVC.controllers.group_controller import group_controller
from PyCharmProject.telegram_bot.MVC.controllers.teacher_controller import teacher_controller
from PyCharmProject.telegram_bot.keyboards.admin_reply_kbs import subjects_kb, teachers_by_subject_kb
from PyCharmProject.telegram_bot.maps.subjects import subjects
from PyCharmProject.telegram_bot.states.commands_states import set_user_states
from PyCharmProject.telegram_bot.texts.admin_u_i_texts.admin_texts import set_group_set_subject_text, \
    set_group_set_teacher_text, set_group_set_date_start_text


async def set_group(message: types.Message, state: FSMContext):
    if message.chat.id != message.from_user.id and admin_controller.is_admin(message.from_user.id) and not group_controller.is_group_init(message.chat.id):
        await message.answer(text=set_group_set_subject_text, reply_markup=subjects_kb())
        await state.set_state(set_user_states.set_subject)

async def set_subject(message:types.Message, state: FSMContext):
    if(message.text == "Отмена"):
        await message.answer(text="Отмена, не забудьте удалить все сообщения или скрыть старые сообщения от новых участников", reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        return
    if(message.text not in subjects):
        await message.answer(text="Нажмите на кнопку для выбора программы")
        return
    await state.set_state(set_user_states.set_teacher)
    await state.update_data(set_subject=message.text)
    await message.answer(text=set_group_set_teacher_text, reply_markup=teachers_by_subject_kb(message.text))

async def set_teacher(message:types.Message, state: FSMContext):
    if(message.text == "Отмена"):
        await message.answer(text="Отмена, не забудьте удалить все сообщения или скрыть старые сообщения от новых участников", reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        return
    data = await state.get_data()
    teachers = teacher_controller.get_short_teachers_names_by_subject(data['set_subject'])
    if(message.text not in teachers):
        await message.answer(text="Нажмите на кнопку для выбора программы")
        return
    await state.set_state(set_user_states.set_date)
    await state.update_data(set_teacher=message.text)
    await message.answer(text=set_group_set_date_start_text, reply_markup=types.ReplyKeyboardRemove())
