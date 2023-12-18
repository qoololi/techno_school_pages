import asyncio
import logging

from aiogram.enums import ContentType
from aiogram.fsm import state
from aiogram.types import ReplyKeyboardRemove

from PyCharmProject.telegram_bot.MVC.controllers.teacher_controller import teacher_controller
from PyCharmProject.telegram_bot.MVC.controllers.admin_controller import admin_controller
from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.commands.register_commands import register_commands
from PyCharmProject.telegram_bot.handlers.user_u_i.States import user_u_i_states
from PyCharmProject.telegram_bot.handlers.user_u_i.register_u_i_router import register_u_i_router
from PyCharmProject.telegram_bot.handlers.user_u_i.user_u_i import user_u_i_start
from PyCharmProject.telegram_bot.texts.start_texts import choosing_ui_text, register_state_text, \
    success_registration_text
from keyboards.base_kbs import start_buttons, register_button
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6618395365:AAGkHB6Ggg0KeIbXhD4SwG18MY4Jq-47dgs')
user_router = Router()

class ChooseUi(StatesGroup):
    choosing_ui = State()


class RegisterInDB(StatesGroup):
    waiting_for_register = State()


async def cmd_start(message: types.Message, state: FSMContext):
    if(message.from_user.id != message.chat.id) :
        return
    if admin_controller.is_admin(message.from_user.id):
        await message.answer(text=choosing_ui_text,
                             reply_markup=start_buttons(
                                 admin_ui_flag=admin_controller.is_admin(tg_user_id=message.from_user.id),
                                 teacher_ui_flag=teacher_controller.is_teacher(tg_user_id=message.from_user.id)))
        await state.set_state(ChooseUi.choosing_ui)
    elif user_controller.is_user_init(message.from_user.id):
        await user_u_i_start(message, state)
    else:
        await message.answer(text=register_state_text(message.from_user.full_name),
                             reply_markup=register_button())
        await state.set_state(RegisterInDB.waiting_for_register)

async def reg_user(message: types.Message, state: FSMContext):
    data = message.web_app_data.data
    data = eval(data)
    data['tg_user_id'] = message.chat.id
    user_controller.set_user(data)
    await message.answer(text=success_registration_text(data), reply_markup=ReplyKeyboardRemove())
    await state.clear()
    await cmd_start(message, state)

# @user_router.callback_query(F.data == 'user_cabinet')
# async def user_cabinet(callback_data: types.CallbackQuery, state: FSMContext ):
#     await callback_data.message.answer(text='fdsfsd')
#     await callback_data.message.edit_text(text="dsad")

async def main():
    dp = Dispatcher()
    dp.message.register(cmd_start, F.text == "/start")
    dp.message.register(reg_user, F.content_type.in_(ContentType.WEB_APP_DATA), RegisterInDB.waiting_for_register)
    register_u_i_router(dp)
    register_commands(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
