import psycopg2
from PyCharmProject.telegram_bot.MVC.db_connection import connection

class group_model:
    @staticmethod
    def get_group_id(chat_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select group_id from groups where chat_id = {chat_id}")
            return cur.fetchone()[0]