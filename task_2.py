import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Функція знаходить усі дійсні числа у тексті та повертає їх як генератор.

    :param text: Текстовий рядок, який містить числа.
    :return: Генератор чисел типу float.
    """
    # Знаходимо всі дійсні числа, відокремлені пробілами
    matches = re.findall(r'\b\d+\.\d+\b', text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, використовуючи функцію генератора чисел.

    :param text: Текстовий рядок з числами.
    :param func: Функція-генератор, яка видобуває числа з тексту.
    :return: Сума всіх чисел у тексті.
    """
    return sum(func(text))



text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями "
            "27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")