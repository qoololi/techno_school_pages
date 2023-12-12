from typing import Dict

choosing_ui_text = "Привет, выбери режим работы"

def register_state_text(name: str) -> str:
    return f"Привет, {name}, мы не нашли тебя в нашей базе(.😔\nПройди регистрацию (кнопочка регистрация)."

def success_registration_text(name: Dict) -> str:
    return f"Поздравляю, {name['last_name']} {name['first_name']} {name['second_name']}, вы успешно зарегистрированы в нашей школе!\n"

def start_messsage_hello(fullname: str) -> str:
    return f"Привет {fullname}."

