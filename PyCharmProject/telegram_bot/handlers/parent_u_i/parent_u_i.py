from aiogram import types
from aiogram.fsm.context import FSMContext

from PyCharmProject.telegram_bot.MVC.controllers.parent_controller import parent_controller
from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.keyboards.callback_factories.child_callback_data import ChildCallbackData
from PyCharmProject.telegram_bot.keyboards.parent_inline_kbs import parent_u_i_start_kb, parent_u_i_cabinet_kb, \
    parent_u_i_children_kb, parent_u_i_child_kb
from PyCharmProject.telegram_bot.texts.parent_texts import parent_u_i_start_text, parent_children_text, \
    parent_child_text


async def parent_u_i_start(message: types.Message):
    await message.answer(text=parent_u_i_start_text(message.from_user.id), reply_markup=parent_u_i_start_kb())


async def parent_u_i_back_to_menu(callback_data: types.CallbackQuery):
    await callback_data.message.answer(text=parent_u_i_start_text(callback_data.message.chat.id),
                                       reply_markup=parent_u_i_start_kb())
    await callback_data.message.delete()


async def parent_cabinet(callback_data: types.CallbackQuery):
    from PyCharmProject.telegram_bot.bot import bot
    photos = await bot.get_user_profile_photos(callback_data.message.chat.id, limit=1)
    photo = max(photos.photos[0], key=lambda x: x.width)
    await callback_data.message.answer_photo(photo=photo.file_id, caption="huesos",
                                             reply_markup=parent_u_i_cabinet_kb())
    await callback_data.message.delete()


async def parent_children(callback_data: types.CallbackQuery):
    await callback_data.message.edit_caption(caption=parent_children_text, reply_markup=parent_u_i_children_kb(
        parent_controller.get_children(callback_data.from_user.id)))

async def parent_u_i_child(query:types.CallbackQuery, callback_data: ChildCallbackData):
    subscribes = user_controller.get_subscribes(tg_user_id=callback_data.tg_child_id)
    # await query.answer(text=str(callback_data))
    await query.message.edit_caption(caption=parent_child_text(tg_child_id=callback_data.tg_child_id, subscribes=subscribes),
                                     reply_markup=parent_u_i_child_kb(callback_data.tg_child_id, subscribes=subscribes))















