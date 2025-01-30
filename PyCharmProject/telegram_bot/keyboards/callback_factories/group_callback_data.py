from aiogram.filters.callback_data import CallbackData


class GroupCallbackData(CallbackData, prefix="user_group"):
    group_id: int
    tg_chat_id: int
