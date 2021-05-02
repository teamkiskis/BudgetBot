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
    ("products", "продукти", true, "їжа"),
    ("coffee", "кава", true, ""),
    ("dinner", "обід", true, "столова, ланч, бізнес-ланч, бізнес ланч"),
    ("cafe", "кава", true, "ресторан, рест, мак, макдональдс, макдак, kfc, ilpatio, il patio"),
    ("transport", "громад. транспор", false, "метро, автобус, metro"),
    ("taxi", "такси", false, "яндекс такси, yandex taxi"),
    ("phone", "телефон", false, "теле2, звязок"),
    ("books", "книги", false, "література, літра, літ-ра"),
    ("internet", "интернет", false, "інет, inet"),
    ("subscriptions", "подписки", false, "подписка"),
    ("other", "інше", true, "");

insert into budget(codename, daily_limit) values ('base', 500);