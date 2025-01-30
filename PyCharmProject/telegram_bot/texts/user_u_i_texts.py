from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller


def u_i_start_text(tg_user_id) -> str:
    names = user_controller.get_user_name(tg_user_id=tg_user_id)
    return (f"Привет, {names[0]} {names[1]} {names[2]}, я дружелюбный помощник онлайн школы TechnoSchool.\n"
            f"Личный кабинет - Личный кабинет ученика\n"
            f"О нас - более подробное описание нашей школы и наших программ обучения\n"
            f"По любым вопросам - @TechnoSchoolSupport")

user_u_i_text_no_groups = "К сожалению вы не состоите ни в одной группе"
user_u_i_text_has_groups = "Ваши группы"

def request_to_add_parent_text(last_name:str, first_name:str, second_name:str):
    return f"{last_name} {first_name} {second_name} хочет добавить вас в список своих детей."


def user_u_i_cancel_parent(tg_user_id: int):
    names = user_controller.get_user_name(tg_user_id=tg_user_id)
    return f"К сожалению, {names[0]} {names[1]} {names[2]}, отменил запрос."

def user_u_i_accept_parent(tg_user_id: int):
    names = user_controller.get_user_name(tg_user_id=tg_user_id)
    return f"{names[0]} {names[1]} {names[2]}, подтвердил запрос. Теперь вы сможете найти его в своем личном кабинете."