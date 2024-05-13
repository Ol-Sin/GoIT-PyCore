import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int):
    # Перевірка валідності вхідних даних
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > max_num - min_num + 1:
        return print("Invalid input parameters.")

    # Генерування унікальних чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    # Сортування та повернення результату
    return sorted(numbers)

# Використання функції
lottery_numbers = get_numbers_ticket(1, 100, 10)
print("Your lottery numbers are:", lottery_numbers)