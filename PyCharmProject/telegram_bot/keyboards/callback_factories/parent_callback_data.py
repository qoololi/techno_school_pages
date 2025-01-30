from aiogram.filters.callback_data import CallbackData


class ParentChildSubscribeCallbackData(CallbackData, prefix="parent_u_i_child_subscribe"):
    tg_child_id: int
    subject_name: str

class ParentChildChooseSubscribe(CallbackData, prefix="parent_u_i_choose_subscribe"):
    tg_child_id: int
    subject_name: str


class ParentChildChooseBundles(CallbackData, prefix="parent_u_i_bundles"):
    tg_child_id: int


class ParentChildChooseConcreteBundle(CallbackData, prefix="parent_subj_bundle"):
    tg_child_id: int
    bundle_ind: int

class ParentChildChooseTermOfSubscribe(CallbackData, prefix="parent_term_subscribe"):
    tg_child_id: int
    subject_name: str
    term:int


class ParentChildChooseTermOfBundle(CallbackData, prefix="parent_term_bundle"):
    tg_child_id: int
    bundle_ind: int
    term:int
