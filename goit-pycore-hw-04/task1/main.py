def total_salary(path):
    total_salary = 0
    total_developers = 0

    try:
        with open(path, "r", encoding='utf-8') as file: # Безпечне відкриття файлу з встановленним кодуванням
            for line in file:
                _, salary = line.strip().split(',') # Виокремлюємо із запису заробітню плату вказуючи роздільник
                total_salary += int(salary) # Оновлюємо загальну сумму заробітьої плати
                total_developers += 1 # Оновлюємо загальну кількість співробітників
                
        if total_developers == 0:
            return 0, 0  # Повертаємо порожні значення, якщо файл порожній

        average_salary = total_salary / total_developers # Розрахунок середньої заробітньої плати
        return total_salary, average_salary # Повернення результату

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None  # Повертаємо None, якщо файл не знайдено

    except ValueError:
        print("Невірний формат файлу.")
        return None, None  # Повертаємо None, якщо неправильний формат файлу

total, average = total_salary("goit-pycore-hw-04/task1/salary_file.txt") # Використання функції
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # Якщо використання функції не повернуло помилку - виводимо результат
