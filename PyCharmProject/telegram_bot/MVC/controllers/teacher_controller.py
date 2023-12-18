import psycopg2
from typing import Any, Dict

from PyCharmProject.telegram_bot.MVC.models.teacher_model import teacher_model
from PyCharmProject.telegram_bot.MVC.models.user_model import user_model


class teacher_controller:

    @staticmethod
    def is_teacher(tg_user_id: int):
        try:
            teacher_model.get_teacher_id(user_model.get_user_id(tg_user_id=tg_user_id))
            return True
        except:
            return False

    @staticmethod
    def get_teachers_by_subject(subject_name: str):
        return teacher_model.get_teachers_by_subject(subject_name=subject_name)

    @staticmethod
    def get_short_teachers_names_by_subject(subject_name: str):
        teachers = teacher_model.get_teachers_by_subject(subject_name=subject_name)
        names = []
        for teacher in teachers:
            names.append(f"teacher_id:{teacher[0]}\n{teacher[1]} {teacher[2][0]}.{teacher[3][0]}.")
        return names
    # def update_teacher_info(self, tg_user_id: int, new_data: Dict[str, Any]) -> bool:
    #     succes_flag = teacher_model.update_teacher_info(tg_user_id, new_data)
    #
    #     return succes_flag
