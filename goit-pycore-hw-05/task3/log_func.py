import re # Імпорт модуля для роботи з регулярними виразами
from collections import Counter # Імпорт підклассу з модуля для роботи з колекціями
from typing import List, Dict # Імпорт классів з модуля для зручнішої роботи зі списками та словниками 

def parse_log_line(line: str) -> dict: # Функція парсингу
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>\w+)\s+(?P<message>.*)' # Паттерн регулярного виразу для виокремлення та групування вмісту рядка
    match = re.match(pattern, line) # Застосовуємо паттерну до рядка
    if match:
        return match.groupdict() # Повертаємо словник з іменованними групами
    else:
        return {}

def load_logs(file_path: str) -> List[dict]: # Функція читання з лог-файлу
    logs = [] # Створюємо список куди потраплять результати парсингу
    try:
        with open(file_path, 'r') as file: # Безпечне відкриття файлу на читання
            for line in file: # Вибірка рядків з файлу для подальшого парсингу
                log = parse_log_line(line.strip()) # Створюємо файл з результатами парсингу
                if log:
                    logs.append(log) # Додаємо опрацьований рядок в кінець списку
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.") # Опрацювання помилки відсутності файлу
    except Exception as e:
        print(f"Помилка: {e}") # Опрацювання решти помилок
    return logs # Повертаємо результат

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]: # Функція фільтрації логів за рівнем
    return [log for log in logs if log['level'] == level] # Перебираємо вміст списку та виокремлюємо рівень помилки за допомогою групи з іменем "level"

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]: # Функція підрахуну записів з відповідним рівнем
    levels = [log['level'] for log in logs] # Перебираємо значення відповідного рівня
    return dict(Counter(levels)) # Використовуємо підкласс для підрахунку об'єктів з певною групою

def display_log_counts(counts: Dict[str, int]): # Функція виводу результату
    """Display log counts in a formatted table."""
    print("Log Level\tCount") # Виводимо шапку виводу
    print("-------------------") # Розділювач шапки виводу
    for level, count in counts.items(): # Перебираємо та виводимо результати
        print(f"{level}\t\t{count}")