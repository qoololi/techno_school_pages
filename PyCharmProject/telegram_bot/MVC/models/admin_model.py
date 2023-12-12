import psycopg2
from typing import Dict, Any

from PyCharmProject.telegram_bot.MVC.db_connection import connection


# from ..MVC_exceptions import MVC_exceptions

class admin_model:
    @staticmethod
    def get_admin_id(tg_user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select user_id from admins where tg_user_id = {tg_user_id}")
            return cur.fetchone()[0]

