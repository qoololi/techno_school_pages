
from PyCharmProject.telegram_bot.MVC.db_connection import connection


class parent_model:
    @staticmethod
    def get_parent_id(tg_user_id: int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select pr.parent_id from parents as pr "
                        f"join users as us on pr.user_id = us.user_id "
                        f"where us.tg_user_id = {tg_user_id}")
            return cur.fetchone()[0]

    @staticmethod
    def get_parent_id_by_user_id(user_id:int) -> int:
        with connection.cursor() as cur:
            cur.execute(f"select parent_id from parents where user_id = {user_id}")
            return cur.fetchone()[0]

    @staticmethod
    def set_parent(tg_user_id: int):
        with connection.cursor() as cur:
            cur.execute(f"insert into parents(user_id) values ("
                        f"(select user_id from users where tg_user_id = {tg_user_id}))")
            connection.commit()

    @staticmethod
    def add_child(parent_id: int, child_user_id: int):
        with connection.cursor() as cur:
            cur.execute(f"select * from parents_children where parent_id = {parent_id} and child_user_id = {child_user_id}")
            if cur.fetchone() is None:
                cur.execute(f"insert into parents_children(parent_id, child_user_id) values ({parent_id}, {child_user_id})")
                connection.commit()

    @staticmethod
    def get_children(tg_user_id: int):
        with connection.cursor() as cur:
            cur.execute(f"select us.last_name, us.first_name, us.second_name, us.user_id, us.tg_user_id from users as us "
                        f"join parents_children as p_c on p_c.child_user_id = us.user_id "
                        f"where p_c.parent_id = {parent_model.get_parent_id(tg_user_id=tg_user_id)}")
            return cur.fetchall()