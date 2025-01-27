import random

random.seed()

CHARACTERS = list('abcdefghijklmnopqrstuvwxyz ')
PAGE_SIZE = 1024
# 1466 characters to write this value
TOTAL_PAGES = len(CHARACTERS) ** PAGE_SIZE


def generate_page(seed: int):
    if seed > TOTAL_PAGES:
        raise ValueError(
            "Seed should not be more than the total amount of possible pages.")
    result = ''
    remaining_seed = seed

    for i in range(PAGE_SIZE):
        position = PAGE_SIZE - 1 - i
        divisor = len(CHARACTERS) ** position
        char_index = remaining_seed // divisor
        result += CHARACTERS[char_index]
        remaining_seed %= divisor

    return result


def random_page_number():
    return random.randint(0, TOTAL_PAGES)
