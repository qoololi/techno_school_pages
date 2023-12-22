from typing import Dict
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
    def is_user_by_name_and_phone_init(last_name: str, first_name:str, second_name: str, phone_number: str) -> bool:
        try:
            user_model.get_user_id_by_name_and_phone(last_name=last_name, first_name=first_name, second_name=second_name, phone_number=phone_number)
            return True
        except:
            return False

    @staticmethod
    def get_user_id(tg_user_id: int) -> int:
        return user_model.get_user_id(tg_user_id=tg_user_id)

    @staticmethod
    def get_user_id_by_name_and_phone(last_name: str, first_name:str, second_name: str, phone_number: str):
        return user_model.get_user_id_by_name_and_phone(last_name=last_name, first_name=first_name, second_name=second_name, phone_number=phone_number)


    @staticmethod
    def set_user(data: Dict) -> None:
        user_model.set_user(data=data)

    @staticmethod
    def get_user_name(tg_user_id: int) -> list:
        return user_model.get_names_from_user(tg_user_id=tg_user_id)

    @staticmethod
    def get_user_groups(tg_user_id: int) -> None or list:
        return user_model.get_user_groups(tg_user_id=tg_user_id)

    @staticmethod
    def get_tg_user_id(user_id: int) -> int:
        return user_model.get_tg_user_id(user_id=user_id)

    @staticmethod
    def get_subscribes(tg_user_id: int) -> list or None:
        return user_model.get_subscribes(tg_user_id=tg_user_id)