from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from PyCharmProject.telegram_bot.keyboards.callback_factories.child_callback_data import ChildCallbackData
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_callback_data import \
    ParentChildSubscribeCallbackData, ParentChildChooseSubscribe, ParentChildChooseBundles, \
    ParentChildChooseConcreteBundle, ParentChildChooseTermOfSubscribe
from PyCharmProject.telegram_bot.keyboards.callback_factories.parent_pay_callback_data import \
    ParentBuyCourseCallbackData, ParentExtensionCourseCallbackData
from PyCharmProject.telegram_bot.maps.subjects import subjects_names, subjects_short_names, subject_bundles, \
    bundles_names


def parent_u_i_start_kb():
    markup = InlineKeyboardBuilder().add(
        types.InlineKeyboardButton(text="Мой личный кабинет",
                                   callback_data='parent_cabinet'))
    markup.add(
        types.InlineKeyboardButton(text="О нас", web_app=types.WebAppInfo(
            url="https://technoschool-workspace.ru/visit.html"))
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)


def parent_u_i_cabinet_kb():
    markup = InlineKeyboardBuilder().add(
        types.InlineKeyboardButton(text="Мои дети.", callback_data='parent_u_i_my_children'))
    markup.add(
        types.InlineKeyboardButton(text="Назад.", callback_data='parent_u_i_start')
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)


def parent_u_i_children_kb(child_data):
    markup = InlineKeyboardBuilder()
    for child in child_data:
        print(child)
        markup.add(
            types.InlineKeyboardButton(text=f"{child[0]} {child[1]} {child[2]}",
                                       callback_data=ChildCallbackData(tg_child_id=child[4]).pack())
        )
    markup.add(
        types.InlineKeyboardButton(text="Добавить ребенка.", callback_data="parent_u_i_add_child")
    )
    markup.add(
        types.InlineKeyboardButton(text="Назад.", callback_data="parent_cabinet")
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)


def parent_u_i_child_kb(child_tg_user_id: int, subscribes: list):
    markup = InlineKeyboardBuilder()
    # оплаченые курсы будут + стата в них и тд
    cnt = 0
    for subscribe in subscribes:
        cnt += 1
        markup.add(
            types.InlineKeyboardButton(text=f"{subjects_names[subscribe[0]]}",
                                       callback_data=ParentChildSubscribeCallbackData(tg_child_id=child_tg_user_id,
                                                                                      subject_name=subscribe[0]).pack())
        )

    markup.add(types.InlineKeyboardButton(
        text="Оплатить курс", callback_data=ParentBuyCourseCallbackData(child_tg_user_id=child_tg_user_id).pack()))
    markup.add(types.InlineKeyboardButton(
        text="Программы обучения.", web_app=types.WebAppInfo(
            url="https://technoschool-workspace.ru/visit.html")))
    markup.add(
        types.InlineKeyboardButton(text="Назад.", callback_data='parent_u_i_my_children')
    )
    if cnt > 0:
        markup.adjust(cnt, 1, 1)
    else:
        markup.adjust(1)
    return markup.as_markup(row_width=1)


def parent_u_i_pay_start_kb(tg_child_id: int):
    markup = InlineKeyboardBuilder()
    for subject in subjects_short_names:
        markup.add(types.InlineKeyboardButton(text=subject[0],
                                              callback_data=ParentChildChooseSubscribe(tg_child_id=tg_child_id,
                                                                                       subject_name=subject[1]).pack()))
    markup.add(
        types.InlineKeyboardButton(text="Бандлы",
                                   callback_data=ParentChildChooseBundles(tg_child_id=tg_child_id).pack())
    )
    markup.add(
        types.InlineKeyboardButton(text="Назад", callback_data=ChildCallbackData(tg_child_id=tg_child_id).pack())
    )
    markup.adjust(2, 2, 2, 1, 1)
    return markup.as_markup(row_width=1)


def parent_u_i_pay_bundles_kb(data: ParentChildChooseBundles):
    markup = InlineKeyboardBuilder()
    cnt = 0
    for bundle in subject_bundles:
        markup.add(
            types.InlineKeyboardButton(text=bundles_names[bundle],
                                       callback_data=ParentChildChooseConcreteBundle(tg_child_id=data.tg_child_id,
                                                                                     bundle_ind=cnt).pack())
        )
        cnt += 1
    markup.add(
        types.InlineKeyboardButton(text="Назад",
                                   callback_data=ParentBuyCourseCallbackData(child_tg_user_id=data.tg_child_id).pack())
    )
    markup.adjust(1)
    return markup.as_markup(row_width=1)


def parent_u_i_pay_course_select_term_kb(data: ParentChildChooseSubscribe):
    markup = InlineKeyboardBuilder()
    markup.add(
        types.InlineKeyboardButton(text="1 месяц",
                                   callback_data=ParentChildChooseTermOfSubscribe(tg_child_id=data.tg_child_id,
                                                                                  subject_name=data.subject_name,
                                                                                  term=1).pack()),
        types.InlineKeyboardButton(text="2 месяца",
                                   callback_data=ParentChildChooseTermOfSubscribe(tg_child_id=data.tg_child_id,
                                                                                  subject_name=data.subject_name,
                                                                                  term=2).pack()),
        types.InlineKeyboardButton(text="3 месяца",
                                   callback_data=ParentChildChooseTermOfSubscribe(tg_child_id=data.tg_child_id,
                                                                                  subject_name=data.subject_name,
                                                                                  term=3).pack()),
        types.InlineKeyboardButton(text="6 месяцев",
                                   callback_data=ParentChildChooseTermOfSubscribe(tg_child_id=data.tg_child_id,
                                                                                  subject_name=data.subject_name,
                                                                                  term=6).pack()),
        types.InlineKeyboardButton(text="Назад",
                                   callback_data=ParentBuyCourseCallbackData(child_tg_user_id=data.tg_child_id).pack())
    )
    markup.adjust(2,2,1)
    return markup.as_markup(row_width=1)
