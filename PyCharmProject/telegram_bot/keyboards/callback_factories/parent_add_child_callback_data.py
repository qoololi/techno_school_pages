from aiogram.filters.callback_data import CallbackData


class AddParentCallbackData(CallbackData, prefix="add_parent"):
    parent_tg_user_id: int
    accept_flag: bool