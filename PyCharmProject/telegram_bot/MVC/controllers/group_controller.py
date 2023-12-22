from PyCharmProject.telegram_bot.MVC.models.group_model import group_model


class group_controller:
    @staticmethod
    def is_group_init(chat_id: int) -> bool:
        try:
            group_model.get_group_id(chat_id=chat_id)
            return True
        except:
            return False

    @staticmethod
    def get_group_id(chat_id: int) -> int:
        return group_model.get_group_id(chat_id=chat_id)

    @staticmethod
    def init_new_group(chat_id:int, teacher_id: int, subject_name: str):
        group_model.init_new_group(chat_id=chat_id, teacher_id=teacher_id, subject_name=subject_name)
