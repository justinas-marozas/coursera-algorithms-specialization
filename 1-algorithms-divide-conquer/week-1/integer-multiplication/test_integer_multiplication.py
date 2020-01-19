import random
from typing import List, Tuple

import nose
from parameterized import parameterized

import integer_multiplication


def test_assignment_question() -> None:
    """See <./README.md>."""
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    expected = a * b

    actual = integer_multiplication.product(a, b)

    assert actual == expected


def generate_int_pairs(n: int) -> List[Tuple[int, int]]:
    """Generate `n` number of integer pairs."""
    boundary = 2**30
    return [
        (
            random.randint(-boundary, boundary),
            random.randint(-boundary, boundary)
        )
        for _ in range(n)
    ]


@parameterized(generate_int_pairs(100))
def test_multiplication_gives_correct_answers(a, b) -> None:
    expected = a * b

    actual = integer_multiplication.product(a, b)

    assert actual == expected


@parameterized([
    (random.randint(0, 9), 1),
    (10, 2),
    (random.randint(10, 19), 2),
    (random.randint(-9, -1), 1),
    (-10, 2),
    (random.randint(1000, 9999), 4),
    (random.randint(10**64, (10**65) - 1), 65)
])
def test_int_length_calculation(n: int, size: int) -> None:
    actual = integer_multiplication.size_base10(n)
    assert actual == size


@parameterized([
    (12345, 3, (12, 345)),
    (
        2718281828459045235360287471352662497757247093699959574966967627,
        32,
        (27182818284590452353602874713526, 62497757247093699959574966967627)
    )
])
def test_int_split(n: int, position: int, expected: Tuple[int, int]) -> None:
    actual = integer_multiplication.split_at(n, position)

    assert actual == expected


if __name__ == '__main__':
    nose.main()
