import string
import random


def is_verify_password(password: str) -> bool:
    pass_len = True if len(password) >= 8 else False
    pass_alpha = False
    pass_digit = False

    for char in password:
        if char.isalpha():
            pass_alpha = True
        elif char.isdigit():
            pass_digit = True

    return True if all([pass_len, pass_alpha, pass_digit]) else False


def generate_password(
    len_password: int = 8,
    is_upper: bool = False,
    is_punctuation: bool = False,
    is_repeate: bool = True
) -> str:

    chars_for_pass = string.ascii_lowercase + string.digits
    chars_for_pass += string.ascii_uppercase if is_upper else ""
    chars_for_pass += string.punctuation if is_punctuation else ""

    password = random.choices(chars_for_pass, k=len_password) if is_repeate else random.sample(chars_for_pass, k=len_password)
    return "".join(password)
