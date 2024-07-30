import json

from files import list_files


def save_pets(pets: list) -> None:
    with open(list_files.PETS, "w", encoding="utf-8") as fh:
        pets = [f"{pet}\n" for pet in pets]
        fh.writelines(pets)


def save_log(log: list) -> None:
    with open(list_files.LOG, "w", encoding="utf-8") as fh:
        log = [f"{loging}\n" for loging in log]
        fh.writelines(log)


def save_employees(employees: dict) -> None:
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh, indent=4)


def save_healed_pets(healed_pets: list) -> None:
    with open(list_files.HEALED_PETS, "w", encoding="utf-8") as fh:
        json.dump(healed_pets, fh, indent=4)


def save_using_commands(using_commands: dict) -> None:
    with open(list_files.USING_COMMANDS, "w", encoding="utf-8") as fh:
        json.dump(using_commands, fh, indent=4)


def save_reviews(reviews: list) -> None:
    with open(list_files.REVIEWS, "w", encoding="utf-8") as fh:
        json.dump(reviews, fh, indent=4)