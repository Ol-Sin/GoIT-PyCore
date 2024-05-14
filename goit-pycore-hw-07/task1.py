from collections import UserDict # Імпортуємо метод для роботи з словниками
from datetime import datetime, timedelta # Імпортуємо метод для роботи з датою

class Field: # Створюємо базовий клас для роботи з даними
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Похідний клас для роботи з іменами
    pass

class Phone(Field): # Похідний клас для роботи з телефонами
    def __init__(self, value):
        if not self.validate_phone(value): # Перевірка номеру
            raise ValueError("Invalid phone number format.")
        super().__init__(value)

    @staticmethod # Використовуємо декоратор для доповнення класу валідацією номера
    def validate_phone(value): # Валідація формату номеру
        return len(value) == 10 and value.isdigit()

class Birthday(Field): # Похідний клас для роботи з днями народження
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date() # Переводимо вміст рядкового запису дня народження та представляємо його у заданому форматі дати
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") # Обробка виключення при хибному форматі

class Record: # Створюємо клас для обробки записів
    def __init__(self, name):
        self.name = Name(name) # Визначаємо ім'я типом класу
        self.phones = [] # Ініціалізуємо номери як список для можливості зберігати декілька номерів
        self.birthday = None # Ініціалізуємо необов'язковий атрибут для дня народження

    def __str__(self): # Описуємо представлення рядка за допомогою магучного методу
        phone_numbers = '; '.join(p.value for p in self.phones) # Створюємо атрибут для номерів як послідовності з використанням роздільника
        if self.birthday: # Перевіряємо чи отримали значення для дня народження
            birthday_info = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" # Атрибут для представлення дня народження у заданому форматі
        else:
            birthday_info = "" # Якщо значення не отримали, робимо його порожнім
        return f"Contact name: {self.name.value}, phones: {phone_numbers}{birthday_info}" # Повертаємо інформацію про запис у зручному форматі


    def add_phone(self, phone): # Метод для додавання номеру до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):  # Метод для видалення (насправді перезапису) номерів у списку
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone): # Метод для оновлення номеру
        if not Phone.validate_phone(new_phone): # Використання класу для валідації номеру
            raise ValueError("Invalid phone number format.")
        for phone in self.phones: # Перевіряємо відповідність старого номеру при оновлені на новий
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone): # Метод для пошуку номера в записі
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday): # Метод для додавання дня народження
        self.birthday = Birthday(birthday) # Визначаємо атрибут як клас

class AddressBook(UserDict): # Клас для словника адресної книги
    def __init__(self):
        self.data = {} # Ініціалізація даних як словника

    def add_record(self, record): # Метод для додавання запису в словник
        self.data[record.name.value] = record

    def find(self, name): # Метод для пошуку запису в словнику
        return self.data.get(name)

    def delete(self, name): # Метод для видалення запису з словника
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self): # Метод для отримання записів з найближчими днями народження
        current_day = datetime.today().date() # Визначаємо поточну дату
        upcoming_birthdays = [] # Ініціалізація списку найближчих днів народження

        for name, record in self.data.items(): # Прохід по записам в словнику за атрибутами
            if record.birthday: # Пошук наявності атрибуту дня народження
                birthday = record.birthday.value # Отримуємо значення дня народження
                birthday = birthday.replace(year=current_day.year) # Замінюємо рік в знайденому значенні на поточний
                if birthday < current_day: # Перевірка чи день народження вже минув
                    birthday = birthday.replace(year=current_day.year + 1) # Якщо так, збільшуємо рік для опрацювання цього запису в майбутньому

                if current_day <= birthday <= current_day + timedelta(days=7): # Задаємо критерії для опрацювання, якщо день народження в найближчі 7 днів від поточної дати
                    if current_day.weekday() < 5 and birthday.weekday() < 5: # Перевіряємо чи днь народження в межах робочих днів на цьому тижні
                        congratulation_date = birthday # Якщо попередні умови виконано - ініціалізуємо атрибут з датою привітання
                        formatted_congratulation_date = congratulation_date.strftime("%A, %d %B") # Атрибут для представлення дати привітання з днем народження у заданому форматі
                        upcoming_birthdays.append({"name": record.name.value, "congratulation_date": formatted_congratulation_date}) # Додаємо запис до списку

        upcoming_birthdays.sort(key=lambda x: datetime.strptime(x["congratulation_date"], "%A, %d %B")) # Відсортовуємо список за датами привітання
        return upcoming_birthdays # Виводимо список найближчих днів народження

def main(): # Метод основної логіки
    book = AddressBook() # Ініціалізація словника як класу

    john_record = Record("John") # Створюємо запис як клас
    john_record.add_phone("1234567890") # Використовуємо метод класу для додавання номеру
    john_record.add_phone("5555555555") # Додаємо ще один номер
    john_record.add_birthday("17.05.1980") # Використовуємо метод класу для додавання дня народження
    book.add_record(john_record) # Використовуємо метод словника для додавання запису

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("15.05.1975")
    book.add_record(jane_record)

    for name, record in book.data.items(): # Пошук та виведення всіх записів з словника
        print(record)

    john = book.find("John") # Пошук в словнику за іменем
    if john:
        john.edit_phone("1234567890", "1112223333") # Редагуємо номер, якщо такий запис існує
        print(john) # Виведення результату

        found_phone = john.find_phone("5555555555") # Пошук номера
        print(f"{john.name.value}: {found_phone}") # Вивід знайденого номера

    # book.delete("Jane") # Видалення запису за іменем

    upcoming_birthdays = book.get_upcoming_birthdays() # Використовуємо метод класу для пошуку найближчих днів народження в словнику
    print("\nUpcoming birthdays:")
    for birthday in upcoming_birthdays: # Формуємо вивід отриманих записів
        print(f"{birthday['name']}: {birthday['congratulation_date']}")

if __name__ == "__main__":
    main() # Ініціалізація основного методу