import psycopg2
from typing import Dict, Any

from PyCharmProject.telegram_bot.MVC.db_connection import connection

class user_model:
    @staticmethod
    def get_user_id(tg_user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select user_id from users where tg_user_id = {tg_user_id}")
            return cur.fetchone()[0]

    @staticmethod
    def get_tg_user_id(user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select tg_user_id from users where user_id = {user_id}")
            return cur.fetchone()[0]

    @staticmethod
    def get_user_id_by_name_and_phone(last_name:str, first_name:str, second_name:str, phone_number:str):
        with connection.cursor() as cur:
            cur.execute(f"select us.user_id from users as us join users_contacts as us_c "
                        f"on us.user_id = us_c.user_id where us.last_name = '{last_name}' and us.first_name = '{first_name}' "
                        f"and us.second_name = '{second_name}' and us_c.phone_number = '{phone_number}'")
            return cur.fetchone()[0]

    @staticmethod
    def set_user(data: Dict) -> None:
        with connection.cursor() as cur:
            cur.execute(f"insert into users(last_name, first_name, second_name, tg_user_id) "
                        f"values('{data['last_name']}', '{data['first_name']}', '{data['second_name']}', {data['tg_user_id']})")
            connection.commit()
            cur.execute(f"select user_id from users where tg_user_id = {data['tg_user_id']}")
            cur.execute(f"insert into users_contacts values ({cur.fetchone()[0]}, '{data['email']}', '{data['phone']}')")
            connection.commit()

    @staticmethod
    def get_names_from_user(tg_user_id: int) -> list:
        with connection.cursor() as cur:
            cur.execute(f"select last_name, first_name, second_name from users "
                        f"where tg_user_id = {tg_user_id}")
            return cur.fetchone()

    @staticmethod
    def get_user_groups(tg_user_id: int) -> None or list:
        with connection.cursor() as cur:
            cur.execute(f"select gr.subject_name, gr.group_id, gr.chat_id from groups as gr "
                        f"where gr.group_id in (select gr.group_id from subscribe where user_id = "
                        f"(select user_id from users where tg_user_id = {tg_user_id}))")
            return cur.fetchall()

    @staticmethod
    def get_subscribes(tg_user_id: int) -> None or list:
        with connection.cursor() as cur :
            cur.execute(f"select sub.subject_name, sub.group_id, sub.sub_date, sub.sub_term, sub.archive_flag, "
                        f"sub.sub_date + sub.sub_term * interval '1 MONTH' from subscribe as sub "
                        f"join users as us on us.user_id = sub.user_id where us.tg_user_id = {tg_user_id}")
            return cur.fetchall()