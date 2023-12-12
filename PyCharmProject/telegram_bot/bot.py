import asyncio
import logging

from aiogram.enums import ContentType
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.web_app import safe_parse_webapp_init_data

from PyCharmProject.telegram_bot.MVC.controllers.teacher_controller import teacher_controller
from PyCharmProject.telegram_bot.MVC.controllers.admin_controller import admin_controller
from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.texts.start_texts import choosing_ui_text, register_state_text, \
    success_registration_text
from keyboards.base_kbs import start_buttons, register_button
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6618395365:AAGkHB6Ggg0KeIbXhD4SwG18MY4Jq-47dgs')
dp = Dispatcher()
user_router = Router()
parent_router = Router()
admin_router = Router()
teacher_router = Router()

class ChooseUi(StatesGroup):
    choosing_ui = State()


class RegisterInDB(StatesGroup):
    waiting_for_register = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    if admin_controller.is_admin(message.from_user.id):
        await message.answer(text=choosing_ui_text,
                             reply_markup=start_buttons(
                                 admin_ui_flag=admin_controller.is_admin(tg_user_id=message.from_user.id),
                                 teacher_ui_flag=teacher_controller.is_teacher(tg_user_id=message.from_user.id)))
        await state.set_state(ChooseUi.choosing_ui)
    # elif user_controller.is_user_init(message.from_user.id):
    #     await message.answer("Hello!")
    else:
        await message.answer(text=register_state_text(message.from_user.full_name),
                             reply_markup=register_button())
        await state.set_state(RegisterInDB.waiting_for_register)


async def reg_user(message: types.Message):
    data = message.web_app_data.data
    data = eval(data)
    data['tg_user_id'] = message.chat.id
    # user_controller.set_user(data)
    await message.answer(text=success_registration_text(data), reply_markup=ReplyKeyboardRemove())


async def main():
    dp.message.register(reg_user, F.content_type.in_(ContentType.WEB_APP_DATA), RegisterInDB.waiting_for_register)


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
