print("Hello world!")
print("Hello Git")

cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update({"nick":"Simon","age":7,"characteristics":"Meow"})
age = cat.get("age")
cat.update(info)
print(cat)


my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, some_data[0])
my_list.reverse()
print(my_list)

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

some_data = None
msg = some_data or "No data returned"
print(msg)

fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")
