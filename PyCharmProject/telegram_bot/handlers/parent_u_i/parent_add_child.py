from aiogram import types
from aiogram.fsm.context import FSMContext

from PyCharmProject.telegram_bot.MVC.controllers.parent_controller import parent_controller
from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.handlers.parent_u_i.parent_u_i import parent_u_i_start
from PyCharmProject.telegram_bot.handlers.user_u_i.connection_to_parent import send_request_to_add_parent
from PyCharmProject.telegram_bot.keyboards.parent_reply_kbs import parent_u_i_add_child_kb
from PyCharmProject.telegram_bot.states.parent_states import parent_u_i_adding_child
from PyCharmProject.telegram_bot.texts.parent_texts import parent_adding_child_text, parent_adding_child_not_found, parent_adding_child_select_user_is_parent, \
    parent_adding_child_found, parent_adding_child_almost_connected

async def parent_add_child(callback_data: types.CallbackQuery, state: FSMContext):
    await callback_data.answer(text="Нажмите на кнопку ")
    await callback_data.message.delete()
    await state.set_state(parent_u_i_adding_child.waiting_webapp_data)
    await state.update_data(message_id=await callback_data.message.answer(text=parent_adding_child_text,
                                                                          reply_markup=parent_u_i_add_child_kb()))


async def parent_add_child_answer(message: types.Message, state: FSMContext):
    await state.set_state(parent_u_i_adding_child.waiting_webapp_data)
    await state.update_data(
        message_id=await message.answer(text=parent_adding_child_text, reply_markup=parent_u_i_add_child_kb()))


async def parent_add_child_cancel(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await parent_u_i_start(message)
    from PyCharmProject.telegram_bot.bot import bot
    await bot.delete_message(message_id=data['message_id'].message_id, chat_id=message.chat.id)
    await message.delete()
    await state.clear()


async def parent_add_child_catching_data(message: types.Message, state: FSMContext):
    from PyCharmProject.telegram_bot.bot import bot
    data = await state.get_data()
    await bot.delete_message(message_id=data['message_id'].message_id, chat_id=message.chat.id)

    data = eval(message.web_app_data.data)

    if (user_controller.is_user_by_name_and_phone_init(last_name=data['last_name'], first_name=data['first_name'],
                                                       second_name=data['second_name'], phone_number=data['phone'])):
        child_user_id = user_controller.get_user_id_by_name_and_phone(
                                                      last_name=data['last_name'], first_name=data['first_name'],
                                                      second_name=data['second_name'], phone_number=data['phone'])
        if parent_controller.is_parent_by_user_id(user_id=child_user_id):
            await state.clear()
            await message.answer(text=parent_adding_child_select_user_is_parent, reply_markup=types.ReplyKeyboardRemove())
            await parent_u_i_start(message)
            await message.delete()
            return
        children=parent_controller.get_children(tg_user_id=message.chat.id)
        for child in children:
            if child[3] == child_user_id:
                await message.answer(text=parent_adding_child_almost_connected(
                    last_name=data['last_name'], first_name=data['first_name'],
                                                      second_name=data['second_name']), reply_markup=types.ReplyKeyboardRemove())
                await state.clear()
                await parent_u_i_start(message)
                await message.delete()
                return
        await message.answer(text=parent_adding_child_found(
            last_name=data['last_name'], first_name=data['first_name'],
            second_name=data['second_name']), reply_markup=types.ReplyKeyboardRemove())
        await send_request_to_add_parent(tg_user_id=user_controller.get_tg_user_id(user_id=child_user_id),parent_tg_user_id=message.chat.id)
        await state.clear()
        await parent_u_i_start(message)
        await message.delete()
    else:
        await state.update_data(
            message_id=await message.answer(
                text=parent_adding_child_not_found(last_name=data['last_name'], first_name=data['first_name'],
                                                   second_name=data['second_name']),
                reply_markup=parent_u_i_add_child_kb()))
        await message.delete()
        return

