import os # Імпорт пакету для роботи з файловою системою
from decorators import * # Імпортуємо модуль який містить функцію-декоратор

@input_error # Огортаємо функцію для додавання контакту функцією-декоратором
def add_contact(args, contacts): # Функція для додавання контакту
    if len(args) != 2: # Перевірка наявності необхідної кількості аргументів для команди
        return "Invalid command. Format: add [name] [phone]"
    name, phone = args # Розділяємо аргументи вводу
    contacts[name] = phone # Індексуємо номер за ім'ям
    save_contacts(contacts) # Виклик функції збереження запису до файлу
    return "Contact added."

@input_error # Огортаємо функцію оновлення номеру функцією-декоратором
def change_contact(args, contacts): # Функція оновлення номеру
    if len(args) != 2:
        return "Invalid command. Format: change [name] [new_phone]"
    name, new_phone = args
    if name not in contacts: # Виводимо повідомлення якщо контакту не існує
        return f"Contact '{name}' not found."
    contacts[name] = new_phone # Оновлення номеру
    save_contacts(contacts)
    return "Contact updated."

@input_error # Огортаємо функцію виводу номеру за ім'ям функцією-декоратором
def show_phone(args, contacts): # Функція виводу номеру за ім'ям
    if len(args) != 1:
        return "Invalid command. Format: phone [name]"
    name = args[0] # Задаємо ввід як аргумент для індексу при пошуку запису
    if name not in contacts: # Перевіряємо наявність запису, якщо запис відсутній - виводимо повідомлення
        return f"Contact '{name}' not found."
    return contacts[name]

def show_all(contacts): # Функція виводу записві з файлу
    if not contacts: # Вивід повідомлення якщо файл порожній
        return "No contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()]) # Проходимося по вмісту списку контактів
    return result

def save_contacts(contacts): # Функція збереження контактів до файлу
    file_path = os.path.join(os.path.dirname(__file__), "contacts.txt") # Визначаємо та задаємо директорію до файлу з контактами в точці входу
    with open(file_path, "w") as file: # Безпечне відкриття файлу для запису
        for name, phone in contacts.items(): # Обробка записві
            file.write(f"{name},{phone}\n") # Додаємо запис до файлу

def load_contacts(): # Функція завантаження файлу з контактами
    file_path = os.path.join(os.path.dirname(__file__), "contacts.txt")
    if not os.path.exists(file_path): # Перевірка наявності файлу з контактами, якщо немає - створюємо
        with open(file_path, "w"): 
            pass
    with open(file_path, "r") as file: # Безпечне відкриття файлу для отримання записів
        contacts = {name: phone.strip() for name, phone in [line.strip().split(",") for line in file]} # Створюємо словник та заповнюємо його даними з файлу
        # Індексом в словнику робимо ім'я і використовуємо індекс та значення як аргументи при виконанні внутрішнього циклу, котрий опрацьовує вміст
        # Зчитуємо кожен рядок з файлу, прибираємо зайві пробіли, використовуючи роздільник виокремлюємо ім'я та номер. В результаті маємо список списків :)
    return contacts

