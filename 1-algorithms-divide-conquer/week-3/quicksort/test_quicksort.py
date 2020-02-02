import random

import nose
from parameterized import parameterized

import quicksort


@parameterized([
    # Basic example.
    ([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 0, 2),
    # Go through sorting steps.
    ([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 3, 4),
    ([4, 2, 3, 1, 5, 8, 7, 6], 0, 5, 2, 2),
    ([1, 2, 3, 4, 5, 8, 7, 6], 5, 7, 7, 5),
    ([1, 2, 3, 4, 5, 6, 7, 8], 0, 2, 1, 1),
    ([1, 2, 3, 4, 5, 6, 7, 8], 6, 7, 6, 6)
])
def test_partition(seq: list, l_i: int, r_i: int, p_i: int, p_i_expected: int) -> None:
    pivot = seq[p_i]

    seq_actual, p_i_actual = quicksort.partition(seq, l_i, r_i, p_i)

    assert p_i_actual == p_i_expected
    assert seq_actual[p_i_expected] == pivot
    assert all(
        x < seq_actual[p_i_expected]
        for x in seq_actual[:p_i_expected]
    )
    assert all(
        x > seq_actual[p_i_expected]
        for x in seq_actual[p_i_expected + 1:]
    )


@parameterized([
    ([x for x in random.sample(range(10), 10)],),
    ([x for x in random.sample(range(100), 100)],),
    ([x for x in random.sample(range(1000), 1000)],),
    ([x for x in random.sample(range(10000), 10000)],),
])
def test_quicksort(seq: list) -> None:
    expected = sorted(seq)

    actual = quicksort.quicksort(seq)

    assert actual == expected


def test_assignment_1() -> None:
    seq = [
        int(x)
        for x in open('./input.txt', mode='r', encoding='utf-8')
    ]
    # Verify the contents of `input.txt` are as expected.
    sorted_seq = sorted(seq)
    assert sorted_seq == list(range(1, 10001))

    actual_seq, actual_n_comparisons = quicksort.quicksort_assignment(seq)

    assert actual_seq == sorted_seq
    print(f'{actual_n_comparisons = }')
    assert actual_n_comparisons == 147218


if __name__ == '__main__':
    nose.main()
