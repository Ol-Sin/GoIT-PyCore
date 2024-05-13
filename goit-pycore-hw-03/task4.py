from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    current_day = datetime.today().date()  # Визначаємо поточну дату
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # Повертаємо день народження, як об'єкт дати
        birthday = birthday.replace(year=current_day.year)  # Заміна року на поточний, для зручності визначення

        # Перевіряємо чи день народження вже минув у цьому році
        if birthday < current_day:
            birthday = birthday.replace(year=current_day.year + 1)

        # Перевіряємо чи день народження відбудеться наступного тижня
        if current_day <= birthday <= current_day + timedelta(days=7):
            # Якщо поточний день є робочим і день народження не припадає на вихідний, додаємо привітання
            if current_day.weekday() < 5 and birthday.weekday() < 5:
                congratulation_date = birthday
                formatted_congratulation_date = congratulation_date.strftime("%A, %d %B")
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": formatted_congratulation_date})

    # Відсортовуємо список привітань за датами народження
    upcoming_birthdays.sort(key=lambda x: datetime.strptime(x["congratulation_date"], "%A, %d %B"))

    return upcoming_birthdays  # Повертаємо результат

users = [
    {"name": "John Doe", "birthday": "1985.04.26"},
    {"name": "Jane Smith", "birthday": "1990.04.23"}
]

# Використання функції
upcoming_birthdays = get_upcoming_birthdays(users)

# Виведення результату після перевірки чи список не порожній
if upcoming_birthdays:
    print(f"Список привітань на цьому тижні: {upcoming_birthdays}")
else:
    print("На цьому тижні немає іменинників")
