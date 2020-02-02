import random
from typing import List, Tuple

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
    """Verify partition step works."""
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
    ([x for x in random.sample(range(1_000), 1_000)],),
    ([x for x in random.sample(range(10_000), 10_000)],),
])
def test_quicksort(seq: list) -> None:
    """Verify QuickSort works."""
    expected = sorted(seq)

    actual = quicksort.quicksort(seq)

    assert actual == expected


def test_random_pivot_picker() -> None:
    l_i = 0
    r_i = 999

    for _ in range(100):
        actual_i = quicksort.pick_random([], l_i, r_i)

        assert l_i <= actual_i < r_i


@parameterized([
    (0, 4, 0),
    (3, 14, 3),
    (234, 3453, 234)
])
def test_leftmost_pivot_picker(l_i: int, r_i: int, expected_i: int) -> None:
    actual_i = quicksort.pick_leftmost([], l_i, r_i)

    assert actual_i == expected_i


@parameterized([
    (0, 4, 3),
    (3, 14, 13),
    (234, 3453, 3452)
])
def test_rightmost_pivot_picker(l_i: int, r_i: int, expected_i: int) -> None:
    actual_i = quicksort.pick_rightmost([], l_i, r_i)

    assert actual_i == expected_i


@parameterized([
    ([3, 8, 2, 5, 1, 4, 7, 6], 3),
    ([5, 8, 2, 3, 1, 4, 7, 6], 0),
    ([3, 8, 2, 8, 1, 4, 7, 5], 7)
])
def test_three_point_median_picker(seq: list, expected_i: int) -> None:
    l_i = 0
    r_i = len(seq)

    actual_i = quicksort.pick_median_from_left_mid_right_points(seq, l_i, r_i)

    print(f'{actual_i = }')
    assert actual_i == expected_i


def test_assignment_1() -> None:
    """See <./README.md>."""
    seq, sorted_seq = get_assignment_input()

    actual_seq, actual_n_comparisons = quicksort.quicksort_assignment(seq, quicksort.pick_leftmost)

    assert actual_seq == sorted_seq
    print(f'{actual_n_comparisons = }')
    assert actual_n_comparisons == 162_085


def test_assignment_2() -> None:
    """See <./README.md>."""
    seq, sorted_seq = get_assignment_input()

    actual_seq, actual_n_comparisons = quicksort.quicksort_assignment(seq, quicksort.pick_rightmost)

    assert actual_seq == sorted_seq
    print(f'{actual_n_comparisons = }')
    assert actual_n_comparisons == 164_123


def test_assignment_3() -> None:
    """See <./README.md>."""
    seq, sorted_seq = get_assignment_input()

    actual_seq, actual_n_comparisons = quicksort.quicksort_assignment(
        seq,
        quicksort.pick_median_from_left_mid_right_points
    )

    assert actual_seq == sorted_seq
    print(f'{actual_n_comparisons = }')
    assert actual_n_comparisons == 138_382


def test_median_picker_does_least_work() -> None:
    seq, _ = get_assignment_input()

    # Succeeded with `range(1_000)` but took forever to complete.
    for _ in range(10):
        _, random_n = quicksort.quicksort_assignment(seq, quicksort.pick_random)
        _, left_n = quicksort.quicksort_assignment(seq, quicksort.pick_leftmost)
        _, right_n = quicksort.quicksort_assignment(seq, quicksort.pick_rightmost)
        _, med_n = quicksort.quicksort_assignment(
            seq,
            quicksort.pick_median_from_left_mid_right_points
        )

        print(f'{random_n = }')
        print(f'{left_n = }')
        print(f'{right_n = }')
        print(f'{med_n = }')
        assert med_n < min(random_n, left_n, right_n)


def get_assignment_input() -> Tuple[List[int], List[int]]:
    seq = [
        int(x)
        for x in open('./input.txt', mode='r', encoding='utf-8')
    ]
    # Verify the contents of `input.txt` are as expected.
    sorted_seq = sorted(seq)
    assert sorted_seq == list(range(1, 10_001))
    return seq, sorted_seq


if __name__ == '__main__':
    nose.main()
