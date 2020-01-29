import nose

import quicksort


def test_partition() -> None:
    seq = [3, 8, 2, 5, 1, 4, 7, 6]

    actual = quicksort.partition(seq, 0, 7)

    pivot = 3
    pos = 2  # index of pivot value
    assert actual[pos] == pivot
    assert all(x < actual[pos] for x in actual[:pos])
    assert all(x > actual[pos] for x in actual[pos + 1:])


if __name__ == '__main__':
    nose.main()
