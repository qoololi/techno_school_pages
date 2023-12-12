from PyCharmProject.telegram_bot.MVC.models.admin_model import admin_model


class admin_controller:
    def __init__(self, teacher_view):
        self.teacher_view = teacher_view

    @staticmethod
    def is_admin(tg_user_id: int):
        try:
            admin_model.get_admin_id(tg_user_id)
            return True
        except:
            return False
