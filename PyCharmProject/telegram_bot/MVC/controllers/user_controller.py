from typing import Dict

import psycopg2


from PyCharmProject.telegram_bot.MVC.models.user_model import user_model


class user_controller:
    @staticmethod
    def is_user_init(tg_user_id: int) -> bool:
        try:
            user_model.get_user_id(tg_user_id=tg_user_id)
            return True
        except:
            return False

    @staticmethod
    def get_user_id(tg_user_id: int) -> int:
        return user_model.get_user_id(tg_user_id=tg_user_id)

    @staticmethod
    def set_user(data: Dict) -> None:
        user_model.set_user(data)

