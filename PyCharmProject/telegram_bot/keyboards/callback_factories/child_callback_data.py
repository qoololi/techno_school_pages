from aiogram.filters.callback_data import CallbackData


class ChildCallbackData(CallbackData, prefix="user_child"):
    tg_child_id: int
