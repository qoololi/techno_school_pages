import psycopg2
from typing import Dict, Any, List

from PyCharmProject.telegram_bot.MVC.db_connection import connection


# from ..MVC_exceptions import MVC_exceptions

class teacher_model:
    @staticmethod
    def set_new_teachet(teacher_user_id: int) -> bool:
        with connection.cursor() as cur:
            try:
                cur.execute(f"insert into teachers values({teacher_user_id})")
                return True
            except:
                connection.rollback()
                return False
    @staticmethod
    def get_teacher_id(user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select teacher_id from teachers where user_id = {user_id}")
            return cur.fetchone()[0]
    @staticmethod
    def set_new_subjects(teacher_id, data: List[str]) -> bool:
        with connection.cursor() as cur:
            try:
                cur.executemany(f"insert into teacher_subject values({teacher_id}, %s)", data)
                connection.commit()
                return True
            except:
                connection.rollback()
                return False

    @staticmethod
    def get_teachers_by_subject(subject_name:str):
        with connection.cursor() as cur:
            cur.execute((f"select tch.teacher_id, us.last_name, us.first_name, us.second_name from teachers as tch "
                            f"join users as us on tch.user_id = us.user_id "
                            f"join teacher_subject as tsub on tch.teacher_id = tsub.teacher_id "
                            f"where tsub.subject_name = '{subject_name}'"))
            return cur.fetchall()
    # def update_teacher_info(self, tg_user_id: int, new_data: Dict[str: Any]):
    #     with self.connection.cursor() as cur:
