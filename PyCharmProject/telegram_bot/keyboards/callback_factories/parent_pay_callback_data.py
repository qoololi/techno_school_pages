from aiogram.filters.callback_data import CallbackData


class ParentBuyCourseCallbackData(CallbackData, prefix="parent_buy_course"):
    child_tg_user_id:int

class ParentExtensionCourseCallbackData(CallbackData, prefix="parent_extension_course"):
    child_tg_user_id: int

