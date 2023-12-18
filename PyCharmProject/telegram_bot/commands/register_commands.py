from aiogram import Router, F
from aiogram.fsm.state import any_state

from PyCharmProject.telegram_bot.commands.admin_commands import set_group, set_subject, set_teacher
from PyCharmProject.telegram_bot.states.commands_states import set_user_states


def register_commands(router: Router):
    router.message.register(set_group, F.text == "/set_group")
    router.message.register(set_subject, set_user_states.set_subject)
    router.message.register(set_teacher, set_user_states.set_teacher)