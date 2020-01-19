import random

import nose

import merge_sort


def test_list_gets_sorted_correctly() -> None:
    to_sort = [random.random() for _ in range(1_000_000)]
    expected = sorted(to_sort)

    actual = merge_sort.merge_sort(to_sort)

    assert actual == expected


if __name__ == '__main__':
    nose.main()
