# from cont_func import *  # Імпортуємо модуль, що містить функції обробки контактів та читання/збереження файлу
# from decorators import *  # Імпортуємо модуль, що містить функцію-декоратор
# from collections import UserDict
# from datetime import datetime, timedelta

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     pass

# class Phone(Field):
#     def __init__(self, value):
#         if not self.validate_phone(value):
#             raise ValueError("Invalid phone number format.")
#         super().__init__(value)

#     @staticmethod
#     def validate_phone(value):
#         return len(value) == 10 and value.isdigit()

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []
#         self.birthday = None  # Додали атрибут birthday

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

#     def add_phone(self, phone):
#         self.phones.append(Phone(phone))

#     def remove_phone(self, phone):
#         self.phones = [p for p in self.phones if p.value != phone]

#     def edit_phone(self, old_phone, new_phone):
#         if not Phone.validate_phone(new_phone):
#             raise ValueError("Invalid phone number format.")
#         for phone in self.phones:
#             if phone.value == old_phone:
#                 phone.value = new_phone
#                 break

#     def find_phone(self, phone):
#         for p in self.phones:
#             if p.value == phone:
#                 return p.value
#         return None
#     def set_birthday(self, birthday):
#         self.birthday = birthday

#     def add_birthday(self, birthday):
#         self.birthday = datetime.strptime(birthday, "%d.%m.%Y")

# class AddressBook(UserDict):
#     def __init__(self):
#         self.data = {}

#     def add_record(self, record):
#         self.data[record.name.value] = record

#     def find(self, name):
#         return self.data.get(name)

#     def delete(self, name):
#         if name in self.data:
#             del self.data[name]

#     def get_upcoming_birthdays(self):
#         current_day = datetime.today().date()
#         upcoming_birthdays = []

#         for name, record in self.data.items():
#             if record.birthday:
#                 birthday = record.birthday
#                 birthday = birthday.replace(year=current_day.year)
#                 if birthday < current_day:
#                     birthday = birthday.replace(year=current_day.year + 1)

#                 if current_day <= birthday <= current_day + timedelta(days=7):
#                     if current_day.weekday() < 5 and birthday.weekday() < 5:
#                         congratulation_date = birthday
#                         formatted_congratulation_date = congratulation_date.strftime("%A, %d %B")
#                         upcoming_birthdays.append({"name": record.name.value, "congratulation_date": formatted_congratulation_date})

#         upcoming_birthdays.sort(key=lambda x: datetime.strptime(x["congratulation_date"], "%A, %d %B"))
#         return upcoming_birthdays

# def parse_input(user_input): # Функція обробки вводу користувача
#     cmd, *args = user_input.split() # Розділяємо ввід користувача на команду та параметри
#     cmd = cmd.strip().lower() # Прибираємо зайві пробіли та переводимо команду до нижнього регістру для уніфікації
#     return cmd, args

# @input_error
# def add_birthday(args, book):
#     if len(args) != 2: # Перевірка наявності необхідної кількості аргументів для команди
#         return "Invalid command. Format: add-birthday [name] [DD.MM.YYYY]"
#     name, birthday = args
#     try:
#         record = book.data.get(name)  # Отримуємо об'єкт Record за ім'ям
#         if record:
#             record.add_birthday(birthday)
#             save_contacts(book.data)  # Зберігаємо зміни у файл
#             return f"Birthday added for {name}."
#         else:
#             # Якщо запис не існує, створюємо новий об'єкт Record і додаємо його до адресної книги
#             record = Record(name)
#             record.add_birthday(birthday)
#             book.add_record(record)
#             save_contacts(book.data)  # Зберігаємо зміни у файл
#             return f"New contact '{name}' created with birthday {birthday}."
#     except ValueError:
#         return "Invalid date format. Please use DD.MM.YYYY format for the birthday."

# @input_error
# def show_birthday(args, book):
#     if len(args) != 1:
#         return "Invalid command. Format: show-birthday [name]"
#     name = args[0]
#     try:
#         birthday = book[name].birthday.strftime("%d.%m.%Y")
#         return f"{name}'s birthday is on {birthday}."
#     except KeyError:
#         return f"Contact '{name}' not found."

# @input_error
# def birthdays(args, book):
#     upcoming_birthdays = book.get_upcoming_birthdays()
#     if not upcoming_birthdays:
#         return "No upcoming birthdays found."
#     return "\n".join([f"{entry['name']}'s birthday is on {entry['congratulation_date']}." for entry in upcoming_birthdays])

# def main(): # Головна функція бота
#         # Приклад ініціалізації контактів як об'єктів Record та їх додавання до адресної книги
#     print("Hello! Welcome to the assistant bot!") # Виводимо привітання від бота

#     contacts = load_contacts()  # Завантажуємо контакти
#     book = AddressBook()  # Створюємо об'єкт адресної книги
#     record1 = Record("John Doe")
#     record1.add_phone("1234567890")
#     record1.add_birthday("15.05.1981")

#     record2 = Record("Jane Smith")
#     record2.add_phone("0987654321")
#     record2.add_birthday("20.07.1975")

#     book.add_record(record1)
#     book.add_record(record2)
#     book.data = contacts  # Завантажуємо контакти в адресну книгу

#     while True:
#         command = input("Enter a command: ").strip().lower() # Отримуємо введену користувачем команду

#         if command in ["close", "exit"]: # Обробляємо вихід з програми
#             print("Good bye!")
#             break

#         elif command == "hello": # Привітання
#             print("How can I help you?")

#         elif command == "help": # Довідка по командам
#             print("""This is what I can help you with working with contacts:
#                   - add (add new contact),
#                   - change (change existing contact),
#                   - phone (show phone by name),
#                   - all (print all contacts I know),
#                   - add-birthday (add birthday for a contact),
#                   - show-birthday (show birthday for a contact),
#                   - birthdays (show upcoming birthdays),
#                   - help (print this message),
#                   - close or exit (end of work)""")

#         else:
#             cmd, args = parse_input(command) # Визначаємо команду та аргументи
#             if cmd == "add":
#                 print(add_contact(args, contacts))
#             elif cmd == "change":
#                 print(change_contact(args, contacts))
#             elif cmd == "phone":
#                 print(show_phone(args, contacts))
#             elif cmd == "all":
#                 print(show_all(contacts))
#             elif cmd == "add-birthday":
#                 print(add_birthday(args, book))
#             elif cmd == "show-birthday":
#                 print(show_birthday(args, book))
#             elif cmd == "birthdays":
#                 print(birthdays(args, book))
#             else:
#                 print("Invalid command.") # Повідомлення про невідому команду

# if __name__ == "__main__": # Перевірка, чи файл є головним скриптом
#     main()

from cont_func import *
from decorators import *
from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return len(value) == 10 and value.isdigit()

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phone_numbers = '; '.join(p.value for p in self.phones)
        birthday_info = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phone_numbers}{birthday_info}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not Phone.validate_phone(new_phone):
            raise ValueError("Invalid phone number format.")
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday):
        if self.birthday:
            return "Birthday already set."
        self.birthday = Birthday(birthday)

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        current_day = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value
                birthday = birthday.replace(year=current_day.year)
                if birthday < current_day:
                    birthday = birthday.replace(year=current_day.year + 1)

                if current_day <= birthday <= current_day + timedelta(days=7):
                    if current_day.weekday() < 5 and birthday.weekday() < 5:
                        congratulation_date = birthday
                        formatted_congratulation_date = congratulation_date.strftime("%A, %d %B")
                        upcoming_birthdays.append({"name": record.name.value, "congratulation_date": formatted_congratulation_date})

        upcoming_birthdays.sort(key=lambda x: datetime.strptime(x["congratulation_date"], "%A, %d %B"))
        return upcoming_birthdays

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Invalid command. Format: add-birthday [name] [DD.MM.YYYY]"
    name, birthday = args
    try:
        record = book.data.get(name)
        if record and hasattr(record, 'add_birthday') and callable(getattr(record, 'add_birthday')):
            record.add_birthday(birthday)
            save_contacts(book.data)
            return f"Birthday added for {name}."
        else:
            return f"Contact '{name}' not found or does not support adding a birthday."
    except ValueError as e:
        return str(e)


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

def main():
    print("Hello! Welcome to the assistant bot!")

    contacts = load_contacts()
    book = AddressBook()

    record1 = Record("John Doe")
    record1.add_phone("1234567890")
    record1.add_birthday("15.05.1981")

    record2 = Record("Jane Smith")
    record2.add_phone("0987654321")
    record2.add_birthday("20.07.1975")

    book.add_record(record1)
    book.add_record(record2)
    book.data = contacts

    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "help":
            print("""This is what I can help you with working with contacts:
                  - add (add new contact),
                  - change (change existing contact),
                  - phone (show phone by name),
                  - all (print all contacts I know),
                  - add-birthday (add birthday for a contact),
                  - show-birthday (show birthday for a contact),
                  - birthdays (show upcoming birthdays),
                  - help (print this message),
                  - close or exit (end of work)""")

        else:
            cmd, args = parse_input(command)
            if cmd == "add":
                print(add_contact(args, contacts))
            elif cmd == "change":
                print(change_contact(args, contacts))
            elif cmd == "phone":
                print(show_phone(args, contacts))
            elif cmd == "all":
                print(show_all(contacts))
            elif cmd == "add-birthday":
                print(add_birthday(args, book))
            elif cmd == "show-birthday":
                print(show_birthday(args, book))
            elif cmd == "birthdays":
                print(birthdays(args, book))
            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()
