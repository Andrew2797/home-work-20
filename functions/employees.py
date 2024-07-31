def add_employee(employees: dict) -> dict:
    login = input("Введіть логін для користувача: ")
    if login in employees:
        print("\nКористувач із таким логіном вже зареєстрований")

    else:
        position = input("Введіть посаду працівника: ")
        salary = int(input("Введіть ЗП: "))
        name = input("Введіть ім'я працівника: ")
        start_date = input("Введіть дату початку роботи у форматі '01.01.2024': ")
        password = input("Створіть пароль для працівника: ")

        employees[login] = {
            "position": position,
            "salary": salary,
            "name" : name,
            "start_date": start_date,
            "password": password
        }

    return employees


def del_employee(employees: dict) -> dict:
    login = input("Введіть логін користавача: ")
    if login in employees:
        del employees[login]
        print("\nКористувача успішно видалено.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees


def show_employees(employees: dict) -> None:
    for login, employee_info in employees.items():
        print(f"'{employee_info['name']}' зареєстрований під логіном '{login}' почав свою роботу '{employee_info['start_date']}'")


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")
    if login in employees:
        print(f"\nПоточне значення ЗП у користувача з логіном '{login}' {employees[login]['salary']}\n")
        employees[login]["salary"] = input("Введіть нове значення ЗП: ")
        print(f"\nКористувачу з логіном '{login}' успішно змінено ЗП.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees


def change_position(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")
    if login in employees:
        print(f"\nПоточна посада працівника '{employees[login]['position']}'")
        employees[login]["position"] = input("Введіть нову посаду: ")
        print("\nПосаду працівника успішно змінено.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees
