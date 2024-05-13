# def greeting():
#     message="Hello world!"
#     print(message)
# greeting()

# def invite_to_event(username):
#     message = f"Dear {username}, we have the honour to invite you to our event"
#     return message
# name = input("Please enter your name: ")
# invite_to_event(name)

# def discount_price(price: float, discount: float = 0) -> float:
#     def apply_discount(discount):
#         nonlocal price
#         price *= (1 - discount)
    
#     apply_discount(discount)
    
#     return price

# price = float(input("Please enter a price: "))
# discount = float(input("Please enter a discount: "))

# new_price = discount_price(price, discount)
# print(f"New price is {new_price}")

# def get_fullname(first_name, last_name, middle_name = ""):
#     if middle_name != "" or middle_name == None:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"
# get_fullname("Alex", "Sinitskyi")
        
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         spaces = (length - len(string)) // 2
#         string = " " * spaces+ string
#         return string
# formatted = format_string("abcde", 17)
# print(formatted)

# def first(size, *args):
#     element = len(args)
#     return size + element
# def second(size, **kwargs):
#     element = len(kwargs)
#     return size + element
# print(first(5, "first", "second", "third"))  # Результат: 8
# print(first(1, "Alex", "Boris"))             # Результат: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
# print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def number_of_groups(n: int, k: int) -> int:
    s = n - k
    result = factorial(n) // (factorial(s) * factorial(k))
    return result

print(number_of_groups(50,7))