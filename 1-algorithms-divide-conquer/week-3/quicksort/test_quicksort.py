import nose
from parameterized import parameterized

import quicksort


@parameterized([
    ([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 0, 2),
    ([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 3, 4)
])
def test_partition(seq: list, l_i: int, r_i: int, p_i: int, p_i_post: int) -> None:
    pivot = seq[p_i]
    actual = quicksort.partition(seq, l_i, r_i, p_i)

    print(f'{actual = }')
    print(f'{p_i_post = }')
    print(f'{pivot = }')
    assert actual[p_i_post] == pivot
    assert all(x < actual[p_i_post] for x in actual[:p_i_post])
    assert all(x > actual[p_i_post] for x in actual[p_i_post + 1:])


if __name__ == '__main__':
    nose.main()
