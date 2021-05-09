<<<<<<< HEAD
"""Сервер Telegram бота, запускаемый непосредственно"""
import logging

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
TOKEN = '1781216379:AAGGPWmURS4M-4ARRZOe5sldLgY2sP6za3E'
import exceptions
import expenses
from categories import Categories
from middlewares import AccessMiddleware



logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Бот для ведення фінансів\n\n"
        "Додати витрати: 250 таксі\n"
        "Сьогоднішня статистика: /today\n"
        "За даний місяць: /month\n"
        "Останні внесені витрати: /expenses\n"
        "Категорії витрат: /categories")


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expense(message: types.Message):
    """Удаляет одну запись о расходе по её идентификатору"""
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    answer_message = "Видалив"
    await message.answer(answer_message)


<<<<<<< HEAD
<<<<<<< HEAD
=======

=======
>>>>>>> Yaroslav-2002-patch-1
@dp.message_handler(commands=['categories'])
async def categories_list(message: types.Message):
    """Отправляет список категорий расходов"""
    categories = Categories().get_all_categories()
    answer_message = "Категорії витрат:\n\n* " +\
            ("\n* ".join([c.name+' ('+", ".join(c.aliases)+')' for c in categories]))
    await message.answer(answer_message)
<<<<<<< HEAD
# papa jhon
=======

>>>>>>> 7a64eb21fb529437b174c9154db95626227d3fd3
=======
>>>>>>> feature/New
>>>>>>> Yaroslav-2002-patch-1

@dp.message_handler(commands=['today'])
async def today_statistics(message: types.Message):
    """Отправляет сегодняшнюю статистику трат"""
    answer_message = expenses.get_today_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['month'])
async def month_statistics(message: types.Message):
    """Отправляет статистику трат текущего месяца"""
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['expenses'])
async def list_expenses(message: types.Message):
    """Отправляет последние несколько записей о расходах"""
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer("Витрати ще не заведені")
        return

    last_expenses_rows = [
        f"{expense.amount} грн. на {expense.category_name} — натисни"
        f"/del{expense.id} для видалення"
        for expense in last_expenses]
    answer_message = "Останні збережені витрати:\n\n* " + "\n\n* "\
            .join(last_expenses_rows)
    await message.answer(answer_message)


@dp.message_handler()
async def add_expense(message: types.Message):
    """Добавляет новый расход"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Додані витрати{expense.amount} грн на {expense.category_name}.\n\n"
        f"{expenses.get_today_statistics()}")
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
=======
logging.basicConfig(level=logging.INFO)
# У поле "TELEGRAM_API_TOKEN" вставте token бота
API_TOKEN = "API_TOKEN"
# У поле "TELEGRAM_ACCESS_ID" вставте свій ID telegram
ACCESS_ID = "ACCESS_ID"

"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
import os

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

import exceptions
import expenses
from categories import Categories
from middlewares import AccessMiddleware

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Відправляє вітальне повідомлення і допомогу по боту"""
    await message.answer(
        "Бот длі обліку фінансів\n\n"
        "Додати витрату: 250 такси\n"
        "Сьогоднішня статистика: /today\n"
        "За поточний місяць: /month\n"
        "Останні внесені витрати: /expenses\n"
        "Категорії витрат: /categories")


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expense(message: types.Message):
    """Видаляє один запис про витрату по її ідентифікатору"""
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    answer_message = "Видалено"
    await message.answer(answer_message)


@dp.message_handler(commands=['categories'])
async def categories_list(message: types.Message):
    """Відправляє список категорій"""
    
    await message.answer("Категорії витрат:\n\n"
"* продукти (їжа, провіант, магазин)\n"
"* обід (столова, ланч, бізнес-ланч, перекус)\n"
"* кафе (ресторан)\n"
"* транспорт (метро, автобус, тролейбус)\n"
"* таксі\n"
"* телефон (поповнення)\n"
"* книги (література, літра, літ-ра)\n"
"* інтернет (інет, inet)\n"
"* підписки\n"
"* розваги\n"
"* одяг\n"
"* ліки\n"
"* метро\n"
"* квартплата\n"
"* одяг\n"
"* інше\n")   



@dp.message_handler(commands=['today'])
async def today_statistics(message: types.Message):
    """Відправляє сьогоднішню статистику витрат"""
    answer_message = expenses.get_today_statistics()
    await message.answer(answer_message)

@dp.message_handler(commands=['week'])
async def week_statistics(message: types.Message):
    """Відправляє статистику витрат поточного місяця"""
    answer_message = expenses.get_week_statistics()
    await message.answer(answer_message)
    
@dp.message_handler(commands=['month'])
async def month_statistics(message: types.Message):
    """Відправляє статистику витрат поточного місяця"""
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['expenses'])
async def list_expenses(message: types.Message):
    """Відправляє останні кілька записів про витрати"""
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer("Витрат немає")
        return

    last_expenses_rows = [
        f"{expense.amount} грн. на {expense.category_name} — натисни "
        f"/del{expense.id} для видалення"
        for expense in last_expenses]
    answer_message = "Останні збережені витрати:\n\n* " + "\n\n* "\
            .join(last_expenses_rows)
    await message.answer(answer_message)


@dp.message_handler()
async def add_expense(message: types.Message):
    """Додає нову витрату"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Додані витрати {expense.amount} грн\n\n"#на {expense.category_name}.\n\n"
        f"{expenses.get_today_statistics()}")
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
>>>>>>> origin/main
