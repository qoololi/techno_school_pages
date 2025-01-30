from PyCharmProject.telegram_bot.MVC.controllers.user_controller import user_controller
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_callback_data import ParentChildChooseSubscribe
from PyCharmProject.telegram_bot.maps.subjects import subjects_names


def parent_u_i_start_text(tg_user_id) -> str:
    names = user_controller.get_user_name(tg_user_id=tg_user_id)
    return (f"Привет, {names[0]} {names[1]} {names[2]}, я дружелюбный помощник онлайн школы TechnoSchool.\n"
            f"Личный кабинет - Личный кабинет родителя\n"
            f"О нас - более подробное описание нашей школы и наших программ обучения\n"
            f"По любым вопросам - @TechnoSchoolSupport")


parent_children_text = "Список ваших детей"
parent_adding_child_text = (
    "Введите в формочку полное фио + номер телефона ребенка.(ребенок должен быть зарегистрирован в нашей системе, в противном случае ему необходимо зарегистрироваться в боте - @TechnoSchool_FriendlyBot)\n"
    "Затем ему придет подтверждение от бота, которое нужно  будет принять.")


def parent_adding_child_found(last_name: str, first_name: str, second_name: str):
    return (f"{last_name} {first_name} {second_name} найден, "
            f"сообщение отправлено. После подтверждения пользователь будет добавлен в список детей, где вы сможете выбрать программу обучения и отслеживать учебный процесс ученика.")


def parent_adding_child_not_found(last_name: str, first_name: str, second_name: str):
    return (f"К сожалению {last_name} {first_name} {second_name} не найден, "
            f"проверьте корректность введенных данных и попробуйте еще раз, или нажмите на кнопку 'Отмена'")


def parent_adding_child_almost_connected(last_name: str, first_name: str, second_name: str):
    return f"{last_name} {first_name} {second_name} уже добавлен в список ваших детей"


parent_adding_child_select_user_is_parent = "Выбранный пользователь был зарегистрирован как родитель, напишите в техподдержку - @TechnoSchoolSupport"


def parent_child_text(tg_child_id: int, subscribes: list):
    names = user_controller.get_user_name(tg_user_id=tg_child_id)
    text = f"🎓Ваш ребенок - {names[0]} {names[1]} {names[2]}.\n"
    if len(subscribes) == 0:
        text += ('Пока не обучается ни в одной программе, для оплаты одной из программ нажмите \'Оплатить курс\'.\n'
                 'Более подробно с нашими программами и ценами можете ознакомиться нажав на кнопку \'Программы обучения\'')
    else:
        text += "Список программ обучения:\n"
        cnt = 0
        for subscribe in subscribes:
            cnt += 1
            if subscribe[4]:
                text += f'◼️{cnt} - {subjects_names[subscribe[0]].lower()}\nЗакончилась - {subscribe[5]}'
            else:
                text += f'📌️{cnt} - {subjects_names[subscribe[0]].lower()}\nОплачена до {subscribe[5]}'

    return text


def get_name_text_by_tg_user_id(tg_user_id: int):
    names = user_controller.get_user_name(tg_user_id=tg_user_id)
    return f"🎓Ваш ребенок - {names[0]} {names[1]} {names[2]}.\n"


def parent_u_i_choose_subscribe_name_text(tg_child_id: int):
    text = get_name_text_by_tg_user_id(tg_user_id=tg_child_id)
    return text + 'Все существующие программы обучения предоставлены снизу.\n(бандлы это наборы, например математика+физика)'


def parent_u_i_choose_bundle_text(tg_child_id: int):
    text = get_name_text_by_tg_user_id(tg_user_id=tg_child_id)
    return text + "Все существующие наборы (бандлы)\n"


def parent_u_i_pay_course_select_term_text(data: ParentChildChooseSubscribe):
    text = get_name_text_by_tg_user_id(tg_user_id=data.tg_child_id)
    return text + f"Выберете продолжительность подписки.\nВыбранный предмет - {subjects_names[data.subject_name].lower()}\n"
