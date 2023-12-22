import psycopg2
from PyCharmProject.telegram_bot.MVC.db_connection import connection

class group_model:
    @staticmethod
    def get_group_id(chat_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select group_id from groups where chat_id = {chat_id}")
            return cur.fetchone()[0]

    @staticmethod
    def init_new_group(chat_id: int, teacher_id: int, subject_name: str):
        with connection.cursor() as cur:
            cur.execute(f"insert into groups(chat_id, teacher_id, subject_name) values({chat_id}, {teacher_id}, '{subject_name}')")
            connection.commit()