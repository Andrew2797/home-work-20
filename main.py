from datetime import datetime
from pprint import pprint

from functions.pets import (
    show_pets,
    add_pet,
    add_pets,
    del_pet_by_name,
    del_pet_by_num,
    sort,
    healed_pets,
    find_pet_by_name,
    show_history,
    palindrome
)
from functions.reviews import add_review, find_dublicate_char
from functions.employees import (
    add_employee,
    del_employee,
    show_employees,
    change_salary,
    change_position
)
from functions.password import is_verify_password, generate_password
from functions import open_files, close_files


def exit(
    pets: list,
    log: list,
    employees: dict,
    healed_pets: list,
    using_commands: dict,
    reviews: list) -> None:

    close_files.save_pets(pets)
    close_files.save_log(log)
    close_files.save_employees(employees)
    close_files.save_healed_pets(healed_pets)
    close_files.save_using_commands(using_commands)
    close_files.save_reviews(reviews)
    print("До побачення")
    quit()


def help() -> None:
    print(open_files.help)


def show_log(log: list) -> None:
    pprint(log)


def show_using_commands(using_commands: dict) -> None:
    pprint(using_commands)


def unknown_command() -> None:
    print("\nНевідома команда. Спробуйте іншу команду.\n")


def main():
    login = input("Введіть свій логін: ")
    employees = open_files.employees
    password = employees.get(login, {}).get("password", "")

    while not password:
        position = input("Введіть посаду працівника: ")
        salary = int(input("Введіть ЗП: "))
        name = input("Введіть ім'я працівника: ")

        employees[login] = {
            "position": position,
            "salary": salary,
            "name" : name,
            "start_date": datetime.now().strftime("%d.%m.%Y")
        }

        command = input("\nВведіть 'create' для введення свого паролю.\n"
                        "Введіть 'generate' для автоматичного створення паролю.\n"
                        "Введіть будь який інший символ для виходу з програми: ")

        if command == "create":
            password = input("Введіть свій пароль. Пароль повинен містити не менше 8 символів, містити принаймні одну літеру та одну цифру\n-> ")

        elif command == "generate":
            len_password = input("Введіть довжину пароль не меншу 8, або залиште за замовчуванням (8 символів): ")
            len_password = int(len_password) if len_password.isdigit() and int(len_password) >= 8 else 8

            is_upper = True if input("Чи використовути великі літери? Введіть 1 - так, будь який інший символ ні: ") == "1" else False
            is_punctuation = True if input("Чи використовути спецсимволи? Введіть 1 - так, будь який інший символ ні: ") == "1" else False
            is_repeate = True if input("Чи можуть символи паролю повторюватись? 1 - так, будь який інший символ - ні: ") == "1" else False


            password = generate_password(
                len_password=len_password,
                is_punctuation=is_punctuation,
                is_upper=is_upper,
                is_repeate=is_repeate
            )

        else:
            print("Ви вийшли з програми")
            break

        if is_verify_password(password):
            employees[login]["password"] = password
            break
        else:
            input("\nПароль не пройшов перевірку. Спробуйте ще раз")

    input(f"Ваш пароль '{password}'. Запам'ятайте його. Натисніть 'enter' для продовження\n")
    pets = open_files.pets
    healed_pets = open_files.healed_pets
    log = open_files.log
    using_commands = open_files.using_commands
    reviews = open_files.reviews

    password_input = input("Введіть пароль для входу в систему: ")

    command = None
    while password == password_input:
        if not command:
            log.append(f"Користувач '{login}' увійшов у систему: {datetime.now()}")
            input("\nПароль введено вірно. Вітаємо нашій інформаційній системі.\n")