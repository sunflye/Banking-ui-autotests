import random


def generate_post_code(length: int = 10) -> str:
    """
    Генерирует случайный код из цифр заданной длины.
    """
    return "".join(random.choices("0123456789", k=length))


def post_code_to_first_name(post_code: str) -> str:
    """
    Преобразует код в строку, которую можно использовать как имя.
    """
    first_name = ""
    for i in range(0, len(post_code), 2):
        pair = int(post_code[i : i + 2])
        letter = chr(ord("a") + (pair % 26))
        first_name += letter
    return first_name
