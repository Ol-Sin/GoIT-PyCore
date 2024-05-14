from datetime import datetime, timedelta
from decorators import input_error
from cont_func import *

@input_error
def add_birthday(args, book):
    if len(args) != 2: # Перевірка наявності необхідної кількості аргументів для команди
        return "Invalid command. Format: add-birthday [name] [DD.MM.YYYY]"
    name, birthday = args
    try:
        record = book.data.get(name)  # Отримуємо об'єкт Record за ім'ям
        if record:
            record.birthday = datetime.strptime(birthday, "%d.%m.%Y")
            save_contacts(book.data)  # Зберігаємо зміни у файл
            return f"Birthday added for {name}."
        else:
            return f"Contact '{name}' not found."
    except ValueError:
        return "Invalid date format. Please use DD.MM.YYYY format for the birthday."

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        return "Invalid command. Format: show-birthday [name]"
    name = args[0]
    try:
        birthday = book[name].birthday.value.strftime("%d.%m.%Y")
        return f"{name}'s birthday is on {birthday}."
    except KeyError:
        return f"Contact '{name}' not found."

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays found."
    return "\n".join([f"{entry['name']}'s birthday is on {entry['congratulation_date']}." for entry in upcoming_birthdays])
