from aiogram import types, F
from aiogram.fsm.context import FSMContext

from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.handlers.user_u_i.States import user_u_i_states
from PyCharmProject.telegram_bot.keyboards.user_inline_kbs import user_u_i_start_kb, user_u_i_cabinet_kb, \
    user_u_i_groups_kb
from PyCharmProject.telegram_bot.texts.user_u_i_texts.user_u_i_texts import u_i_start_text, user_u_i_text_no_groups, \
    user_u_i_text_has_groups


async def user_u_i_start(message: types.Message, state: FSMContext):
    await state.set_state(user_u_i_states.user_menu)
    await message.answer(text=u_i_start_text(message.from_user.id), reply_markup=user_u_i_start_kb())


async def user_u_i_back_to_menu(callback_data: types.CallbackQuery, state:FSMContext):
    await state.set_state(user_u_i_states.user_menu)
    await callback_data.message.answer(text=u_i_start_text(callback_data.message.chat.id), reply_markup=user_u_i_start_kb())
    await callback_data.message.delete()

async def user_cabinet(callback_data: types.CallbackQuery, state: FSMContext ):
    from PyCharmProject.telegram_bot.bot import bot
    photos = await bot.get_user_profile_photos(callback_data.message.chat.id, limit=1)
    photo = max(photos.photos[0], key=lambda x: x.width)
    await state.set_state(user_u_i_states.user_personal_cabinet)
    await callback_data.message.answer_photo(photo=photo.file_id, caption="huesos", reply_markup=user_u_i_cabinet_kb())
    await callback_data.message.delete()

async def user_groups(callback_data: types.CallbackQuery, state: FSMContext):
    groups = user_controller.get_user_groups(callback_data.from_user.id)
    await state.set_state(user_u_i_states.user_groups)
    if len(groups) == 0:
        await callback_data.message.edit_caption(caption=user_u_i_text_no_groups)
    else:
        await callback_data.message.edit_caption(caption=user_u_i_text_has_groups, reply_markup=user_u_i_groups_kb(groups))
