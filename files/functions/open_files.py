import os
import json

from files import list_files


with open(list_files.HELP, "r", encoding="utf-8") as fh:
    help = fh.read()

if not os.path.exists(list_files.PETS):
    with open(list_files.PETS, "w", encoding="utf-8"):
        pass

with open(list_files.PETS, "r", encoding="utf-8") as fh:
    pets = [pet.strip() for pet in fh.readlines()]

if not os.path.exists(list_files.LOG):
    with open(list_files.LOG, "w", encoding="utf-8"):
        pass

with open(list_files.LOG, "r", encoding="utf-8") as fh:
    log = [loging.strip() for loging in fh.readlines()]

if not os.path.exists(list_files.EMPLOYEES):
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump({}, fh)

with open(list_files.EMPLOYEES, "r", encoding="utf-8") as fh:
    employees = json.load(fh)

if not os.path.exists(list_files.HEALED_PETS):
    with open(list_files.HEALED_PETS, "w", encoding="utf-8") as fh:
        json.dump([], fh)

with open(list_files.HEALED_PETS, "r", encoding="utf-8") as fh:
    healed_pets = json.load(fh)

if not os.path.exists(list_files.USING_COMMANDS):
    with open(list_files.USING_COMMANDS, "w", encoding="utf-8") as fh:
        json.dump({}, fh)

with open(list_files.USING_COMMANDS, "r", encoding="utf-8") as fh:
    using_commands = json.load(fh)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as fh:
        json.dump([], fh)

with open(list_files.REVIEWS, "r", encoding="utf-8") as fh:
    reviews = json.load(fh)