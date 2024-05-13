from datetime import datetime

current_date = datetime.today()

def get_days_from_today(date_string):
    try:
        # Перевіряємо формат дати
        target_date = datetime.strptime(date_string, "%Y-%m-%d")
        
        # Розраховуємо різницю між поточною датою та введеною датою у днях, як ціле число
        difference = current_date.toordinal() - target_date.toordinal()
        
        # Повертаємо кількість днів
        return difference
    except ValueError:
        # Повертаємо None якщо нічого не було введено, або не вірний формат вводу
        return None

# Введення дати
date_input = input("Enter a date in YYYY-MM-DD format: ")

# Виклик функції та виведення результату
result = get_days_from_today(date_input)
if result == 0: # Було введено сьогоднішню дату
    print(f"The entered date is Today")
elif result < 0: # Було введено майдутню дату
    print(f"Your input is a future day")
elif result is not None: # Виведення результату
    print(f"The entered date is {result} days far from the current date.")
else: # Порожня дата або не вірний формат вводу
    print("Incorrect date format.")