
from PyCharmProject.telegram_bot.MVC.models.parent_model import parent_model
from PyCharmProject.telegram_bot.MVC.models.user_model import user_model


class parent_controller:
    @staticmethod
    def is_parent(tg_user_id: int) -> bool:
        try:
            parent_model.get_parent_id(tg_user_id=tg_user_id)
            return True
        except:
            return False

    @staticmethod
    def is_parent_by_user_id(user_id:int) -> bool:
        try:
            parent_model.get_parent_id_by_user_id(user_id=user_id)
            return True
        except:
            return False

    @staticmethod
    def get_parent_id(tg_user_id: int) -> int:
        return parent_model.get_parent_id(tg_user_id=tg_user_id)

    @staticmethod
    def set_parent(tg_user_id: int):
        parent_model.set_parent(tg_user_id=tg_user_id)

    @staticmethod
    def add_child(parent_tg_user_id: int, child_tg_user_id: int):
        child_user_id = user_model.get_user_id(tg_user_id=child_tg_user_id)
        parent_id = parent_controller.get_parent_id(tg_user_id=parent_tg_user_id)
        parent_model.add_child(parent_id=parent_id, child_user_id=child_user_id)

    @staticmethod
    def get_children(tg_user_id: int):
        return parent_model.get_children(tg_user_id=tg_user_id)