import nose
from parameterized import parameterized

import inversion_count


@parameterized([
    ([1, 2, 3, 4, 5, 6], 0),
    ([2, 1, 3, 4, 5, 6], 1),
    ([1, 2, 3, 4, 6, 5], 1),
    ([1, 3, 5, 2, 4, 6], 3),
    ([6, 5, 4, 3, 2, 1], 15)
])
def test_inversions_are_counted_correctly(seq, expected) -> None:
    actual, _ = inversion_count.count_inversions(seq)

    assert actual == expected


def test_assignment_file() -> None:
    numbers = [
        int(number)
        for number in open('shuffled-integers.txt', mode='r', encoding='utf-8')
    ]

    actual, _ = inversion_count.count_inversions(numbers)

    print(f'{actual = }')
    assert actual == 2407905288


if __name__ == '__main__':
    nose.main()
