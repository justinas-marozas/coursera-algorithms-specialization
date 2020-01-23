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


if __name__ == '__main__':
    nose.main()
