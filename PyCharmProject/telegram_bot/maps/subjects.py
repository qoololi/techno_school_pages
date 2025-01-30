subjects = {
    'phys_oge',
    'phys_ege',
    'maths_oge',
    'maths_ege',
    'inf_oge',
    'inf_ege'
}

subjects_names = {
    'phys_oge' : "Подготовка к огэ по физике.",
    'phys_ege': "Подготовка к егэ по физике.",
    'maths_oge': "Подготовка к огэ по математике.",
    'maths_ege': "Подготовка к егэ по математике.",
    'inf_oge' : "Подготовка к огэ по информатике.",
    'inf_ege' : "Подготовка к егэ по информатике."
}


subjects_short_names=(
    ("Егэ по физике.", 'phys_ege'),
    ('Егэ по проф. математике.', 'maths_ege'),
    ('Егэ по информатике.', 'inf_ege'),
    ("Огэ по физике.", 'phys_oge'),
    ('Огэ по математике.', 'maths_oge'),
    ('Огэ по информатике.', 'inf_oge')
)

subject_bundles=(
    ('maths_ege', 'phys_ege'),
    ('maths_ege', 'inf_ege'),
    ('phys_ege', 'inf_ege'),
    ('maths_ege', 'phys_ege', 'inf_ege'),
    ('maths_oge', 'phys_oge'),
    ('maths_oge', 'inf_oge'),
    ('phys_oge', 'inf_oge'),
    ('maths_oge', 'inf_oge', 'phys_oge')

)

bundles_names={
    ('maths_ege', 'phys_ege'): "Егэ по проф. математике и физике",
    ('maths_ege', 'inf_ege'): "Егэ по проф. математике и информатике",
    ('phys_ege', 'inf_ege'): "Егэ по физике и информатике",
    ('maths_ege', 'phys_ege', 'inf_ege'):"Егэ по проф. математике, физике и информатике",
    ('maths_oge', 'phys_oge'): "Огэ по математике и физике",
    ('maths_oge', 'inf_oge'): "Огэ по математике и информатике",
    ('phys_oge', 'inf_oge'): "Огэ по физике и информатике",
    ('maths_oge', 'inf_oge', 'phys_oge'):"Огэ по математике, физике и информатике"

}
