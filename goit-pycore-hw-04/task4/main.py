from cont_func import * # Імпортуємо модуль який містить функції обробки контактів та читання/збереження файлу

def parse_input(user_input): # Функція обробки вводу користувача
    cmd, *args = user_input.split() # Розділяємо ввід користувача, як команду та параметри
    cmd = cmd.strip().lower() # Прибираємо зайві пробіли та зводимо введену команду до нижнього регістру щоб мінімізувати похибку введених даних
    return cmd, args

def main(contacts): # Головна функція бота
    print("Hello! Welcome to the assistant bot!") # Виводимо привітання від бота

    while True:
        command = input("Enter a command: ").strip().lower() # Отримання вводу від користувача

        if command in ["close", "exit"]: # Обробка виходу з боту
            print("Good bye!")
            break

        elif command == "hello": # Ініціація привітання
            print("How can I help you?")

        elif command == "help": # Вивід довідки по поточним можливостям боту
            print("""This is what I can help you with working with contacts:
                  - add (add new contact),
                  - change (change existing contact),
                  - phone (show phone by name),
                  - all (print all contacts I know),
                  - help (print this message),
                  - close or exit (end of work)""")

        else:
            cmd, args = parse_input(command) # Визначаєто яку функцію ініціює користувач
            if cmd == "add":
                print(add_contact(args, contacts))
            elif cmd == "change":
                print(change_contact(args, contacts))
            elif cmd == "phone":
                print(show_phone(args, contacts))
            elif cmd == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.") # Вивід повідомлення коли команда не відповідає поточному функціоналу

if __name__ == "__main__": # Перевіряємо, чи запущено цей файл як основний скрипт
    contacts = load_contacts()  # Виклик функції load_contacts() для перевірки наявності файлу з контактами
    main(contacts) # Запускаємо основну функцію
