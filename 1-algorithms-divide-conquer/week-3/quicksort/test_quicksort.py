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
def test_partition(seq: list, l_i: int, r_i: int, p_i: int, p_i_post: int) -> None:
    pivot = seq[p_i]

    actual = quicksort.partition(seq, l_i, r_i, p_i)

    assert actual[p_i_post] == pivot
    assert all(x < actual[p_i_post] for x in actual[:p_i_post])
    assert all(x > actual[p_i_post] for x in actual[p_i_post + 1:])


if __name__ == '__main__':
    nose.main()
