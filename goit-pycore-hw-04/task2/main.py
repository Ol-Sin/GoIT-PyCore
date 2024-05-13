import csv

def get_cats_info(path):
    parsed_cats = []

    try:
        with open(path, "r", encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 3:  # Перевірка формату рядка
                    cat_id, cat_name, cat_age = row
                    parsed_cats.append({"id": cat_id, "name": cat_name, "age": cat_age})
                else:
                    print("Невірний формат рядка:", row)
            return parsed_cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except Exception as e:
        print("Сталася помилка:", e)
        return []

cats_info = get_cats_info("goit-pycore-hw-04/task2/cats_file.txt")
print("Інформація про котів:")
for cat in cats_info:
    print(f"ID: {cat['id']} \tName: {cat['name']} \tAge: {cat['age']}")
