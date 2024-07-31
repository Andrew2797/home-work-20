def show_pets(pets: list) -> None:
    delimeter = "-" * 28
    template = "|{:<5}|{:<20}|"
    print(delimeter)
    print(template.format("№", "Назва тваринки"))
    print(delimeter)
    for i, pet in enumerate(pets, start=1):
        print(template.format(i, pet))
    print(delimeter)


def add_pet(pets: list) -> list:
    pet = input("Введіть нову твармнку для додавання до списку: ")

    if pet not in pets:
        pets.append(pet)
        print(f"\nТваринка '{pet}' додана до списку")
    else:
        print("\nТака тваринка вже є у списку")

    return pets


def add_pets(pets: list) -> list:
    pets = input("Введіть список тваринок для додавання через пробіл\n-> ")
    pets = pets.split()
    pets.extend(pets)
    print("\nСписок тваринок розширено")
    return pets


def del_pet_by_name(pets: list) -> list:
    pet = input("Введіть назву тваринки для видалення зі списку тваринок: ")

    if pet in pets:
        pets.remove(pet)
        print(f"\nТваринка '{pet}' видалено зі списку")
    else:
        print("\nТакої тваринки немає у списку")

    return pets


def del_pet_by_num(pets: list[str]) -> list[str]:
    index = input("Введіть номер тваринки для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(pets):
        pet = pets.pop(int(index) - 1)
        print(f"Тваринка '{pet}' видалено ")
    else:
        print("Ви ввели не вірний номер тваринки")

    return pets


def sort(pets: list) -> None:
    print()
    pets = sorted(pets)
    for pet in pets:
        print(pet)


def healed_pets(pets: list[str], Healed_pets: list[str]) -> tuple:
    pet = input("Введіть назву тваринки для вилікування: ")

    if pet in pets:
        pets.remove(pet)
        healed_pets.append(pet)
        print(f"\nТваринка '{pet}' вилікувана")
    else:
        print("\nТакої тваринки немає у списк")

    return pets, healed_pets


def find_pet_by_name(pets: list) -> None:
    pet = input("Введіть назву тваринки для пошуку: ")

    if pet in pets:
        index = pets.index(pet)
        print(f"Тваринка '{pet}' знаходиться під номером {index + 1}")
    else:
        print("\nТакої тваринки немає у списку")


def show_history(healed_pets: list) -> None:
    healed_pets = healed_pets[::-1]
    for pet in healed_pets:
        print(pet)


def palindrome(pets: list) -> None:
    palin_pets = [pet for pet in pets if pet.lower() == pet[::-1].lower()]
    print(f"\nУ списку з тваринок є такі слова-паліндроми: {palin_pets}\n")
    