from log_func import * # Імпортуємо всі функії для роботи з лог-файлом з модуля log_func
import argparse # Імпортуємо модуль для зручносі парсингу аргументів з консолі

if __name__ == "__main__": # Задаємо єдину точку входу
    

    parser = argparse.ArgumentParser(description="Log Analyzer") # Створюємо парсер аргументів з консолі

    parser.add_argument("file_path", type=str, help="Посилання на лог-файл") # Додаємо шлях до файлу аргументом для парсера
    parser.add_argument("-l", "--level", type=str, help="Рівень логування для фільтрації (наприклад, INFO, ERROR)") # Додаємо рівень логування аргументом для парсера

    args = parser.parse_args() # Використовуємо парсер аргументів

    logs = load_logs(args.file_path) # Використання функції для читання з лог-файлу

    if args.level:
        logs = filter_logs_by_level(logs, args.level.upper()) # Фільтрація записів за рівнем, якщо задано в консолі, то лише зазначеного, якщо ні то фільтруємо все

    counts = count_logs_by_level(logs) # Використання фунуції підрахунку записів за рівнем, якщо задано в консолі, то лише зазначеного, якщо ні то рахуємо всі

    display_log_counts(counts) # Використання функції для виводу результату
