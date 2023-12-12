import psycopg2
from typing import Any, Dict

from PyCharmProject.telegram_bot.MVC.models.teacher_model import teacher_model
from PyCharmProject.telegram_bot.MVC.models.user_model import user_model


class teacher_controller:
    def __init__(self, teacher_view):
        self.teacher_view = teacher_view

    @staticmethod
    def is_teacher(tg_user_id: int):
        try:
            teacher_model.get_teacher_id(user_model.get_user_id(tg_user_id=tg_user_id))
            return True
        except:
            return False

    # def update_teacher_info(self, tg_user_id: int, new_data: Dict[str, Any]) -> bool:
    #     succes_flag = teacher_model.update_teacher_info(tg_user_id, new_data)
    #
    #     return succes_flag
