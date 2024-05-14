from collections import UserDict # Імпортуємо метод для роботи з словниками

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

class Record: # Створюємо клас для обробки записів
    def __init__(self, name):
        self.name = Name(name) # Визначаємо ім'я типом класу
        self.phones = [] # Ініціалізуємо номери як список для можливості зберігати декілька номерів

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" # Описуємо представлення рядка за допомогою магучного методу

    def add_phone(self, phone): # Метод для додавання номеру до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): # Метод для видалення (насправді перезапису) номерів у списку
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

def main(): # Метод основної логіки
    book = AddressBook() # Ініціалізація словника як класу

    john_record = Record("John") # Створюємо запис як клас
    john_record.add_phone("1234567890") # Використовуємо метод класу для додавання номеру
    john_record.add_phone("5555555555") # Додаємо ще один номер
    book.add_record(john_record) # Використовуємо метод словника для додавання запису

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items(): # Пошук та виведення всіх записів з словника
        print(record)

    john = book.find("John") # Пошук в словнику за іменем
    if john:
        john.edit_phone("1234567890", "1112223333") # Редагуємо номер, якщо такий запис існує
        print(john) # Виведення результату

        found_phone = john.find_phone("5555555555") # Пошук номера
        print(f"{john.name.value}: {found_phone}") # Вивід знайденого номера

    book.delete("Jane") # Видалення запису за іменем

if __name__ == "__main__":
    main() # Ініціалізація основного методу