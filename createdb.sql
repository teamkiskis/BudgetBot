create table budget(
    codename varchar(255) primary key,
    daily_limit integer
);

create table category(
    codename varchar(255) primary key,
    name varchar(255),
    is_base_expense boolean,
    aliases text
);

create table expense(
    id integer primary key,
    amount integer,
    created datetime,
    category_codename integer,
    raw_text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

insert into category (codename, name, is_base_expense, aliases)
values
    ("products", "продукти", true, "їжа, провіант, магазин"),
    ("coffee", "кофе", true, ""),
    ("dinner", "обід", true, "столова, ланч, бізнес-ланч, перекус"),
    ("cafe", "кафе", true, "ресторан"),
    ("transport", "транспорт", false, "метро, автобус, тролейбус"),
    ("taxi", "таксі", false, ""),
    ("phone", "телефон", false, "поповнення"),
    ("books", "книжки", false, "література, літра, літ-ра"),
    ("internet", "інтернет", false, "інет, inet"),
    ("subscriptions", "підписки", false, ""),
    ("payments", "квартплата", false, ""),
    ("medicine", "ліки", false, ""),
    ("entertainment", "розваги", false, ""),
    ("clothes", "одяг", false, ""),
    ("other", "інше", false, "");          
     

insert into budget(codename, daily_limit) values ('base', 500);