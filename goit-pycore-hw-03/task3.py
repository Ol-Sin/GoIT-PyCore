import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    digits_only = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо чи номер починається з міжнародного коду, якщо його немає - додаємо
    if not digits_only.startswith('38') and len(digits_only) == 10:
        digits_only = '38' + digits_only
    
    # Додаємо символ '+' на початку номеру
    normalized_number = '+' + digits_only
    
    # Повертаємо нормалізоване значення номеру
    return normalized_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "+    0501112233",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Викликаємо функцію та виводимо результат
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)