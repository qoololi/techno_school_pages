from PyCharmProject.telegram_bot.MVC.db_connection import connection
from PyCharmProject.telegram_bot.MVC.models.group_model import group_model


class group_controller:
    def __init__(self, model=group_model(connection)):
        self.model = model
