import re # Імпортуємо метод для роботи в регулярними виразами
from typing import Callable # Імпортуємо метод для роботи з функціями, як аргументами

def generator_numbers(text: str): # Створюємо функцію-генератор
    numbers = re.findall(r'\b\d+\.\d+\b', text) # Знаходимо всі дійсні числа у тексті за допомогою регулярного виразу
    for number in numbers: # Проходимо по знайденим числам та повертаємо їх як генератор
        yield float(number)

def sum_profit(text: str, func: Callable): # Створюємо функцію для отримання суми з чисел в тексті
    num_gen = func(text) # Отримуємо генератор чисел з тексту
    total_sum = sum(num_gen) # Підсумовуємо всі числа з генератора
    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers) # Виклик функції
print(f"Загальний дохід: ${total_income}") # Виведення результату
