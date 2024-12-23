# ⊗pyPmUFAdv

# №1
from typing import overload


@overload
def multiply(number_1: int, number_2: int) -> int:
    ...


@overload
def multiply(number_1: float, number_2: float) -> float:
    ...


def multiply(number_1: int | float, number_2: int | float) -> int | float:
    return number_1 * number_2


# №2
def say_bye(name: str) -> str:
    return "bye, " + name


# №3
from typing import overload


@overload
def to_string(number: int) -> str:
    ...


@overload
def to_string(number: float) -> str:
    ...


def to_string(number: int | float) -> str:
    return str(number)


# №4
from typing import Sequence, overload


@overload
def sum_positive(lst: list[int]) -> int:
    ...


@overload
def sum_positive(lst: list[float]) -> float:
    ...


def sum_positive(lst: Sequence[int | float]) -> int | float:
    total = 0

    for number in lst:
        if number > 0:
            total += number

    return total
