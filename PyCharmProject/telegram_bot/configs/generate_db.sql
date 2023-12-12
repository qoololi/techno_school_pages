create table if not exists groups
(
    group_id           serial
        primary key,
    chat_id            bigint,
    subject_name       text,
    start_date         timestamp,
    num_of_students    integer default 0,
    teacher_id         integer,
    first_lesson_date  text,
    second_lesson_date text
);

create table if not exists subscribe
(
    user_id      integer not null,
    subject_name text    not null,
    group_id     integer not null,
    sub_date     timestamp,
    sub_term     integer,
    archive_flag boolean default false,
    primary key (user_id, subject_name, group_id)
);


create table if not exists users
(
    user_id     serial
        primary key,
    first_name  text,
    second_name text,
    last_name   text,
    child_id    integer,
    tg_user_id  bigint,
    admin_flag  boolean default false,
    tg_chat_id  bigint
);


create table if not exists teachers
(
    teacher_id   serial
        primary key,
    user_id      integer,
    telegram_teg text
);


create table if not exists admins
(
    user_id    integer,
    tg_user_id bigint
);


create table if not exists teacher_subject
(
    teacher_id   integer,
    subject_name text
);

create table if not exists users_contacts
(
    user_id integer,
    email text,
    phone_number text
);