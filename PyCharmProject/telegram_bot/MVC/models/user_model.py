import psycopg2
from typing import Dict, Any

from PyCharmProject.telegram_bot.MVC.db_connection import connection


# from ..MVC_exceptions import MVC_exceptions

class user_model:
    @staticmethod
    def get_user_id(tg_user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select user_id from users where tg_user_id = {tg_user_id}")
            return cur.fetchone()[0]

    @staticmethod
    def set_user(data: Dict) -> None:
        with connection.cursor() as cur:
            cur.execute(f"insert into users(last_name, first_name, second_name, tg_user_id) "
                        f"values('{data['last_name']}', '{data['first_name']}', '{data['second_name']}', {data['tg_user_id']})")
            cur.execute(f"select user_id from users where tg_user_id = {data['tg_user_id']}")
            cur.execute(f"insert into users_contacts values ({cur.fetchone()[0]}, '{data['email']}', '{data['phone']}')")
            connection.commit()

    # def set_new_user(self, ):