import math
from typing import Tuple


def product(a: int, b: int) -> int:
    "Calculate the product of given integers in a fancy way."
    return karatsuba(a, b)


def karatsuba(a: int, b: int) -> int:
    """Multiply two integers using Karatsuba algorithm.

    See: https://en.wikipedia.org/wiki/Karatsuba_algorithm
    """
    print((a, b))

    if a < 10 or b < 10:
        return a * b

    size = min(size_base10(a), size_base10(b))
    split_position = math.floor(size / 2)

    high_a, low_a = split_at(a, split_position)
    high_b, low_b = split_at(b, split_position)

    z0 = karatsuba(low_a, low_b)
    z1 = karatsuba((low_a + high_a), (low_b + high_b))
    z2 = karatsuba(high_a, high_b)

    return (z2 * 10**(split_position * 2)) + ((z1 - z2 - z0) * 10**split_position) + z0


def size_base10(n: int) -> int:
    """Return the length of a given integer in base 10."""
    n_abs = abs(n)
    size = 1
    while 10**size <= n_abs:
        size += 1
    return size


def split_at(n: int, position: int) -> Tuple[int, int]:
    """Visually split the given integer at the given position.

    :param n: Integer.
    :param position: Position at which to perform a visual split.
    :returns: Two integers resulting from a visual split.
    """
    return divmod(n, 10**position)
