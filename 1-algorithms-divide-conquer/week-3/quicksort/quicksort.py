import random
from typing import Tuple


def quicksort(seq: list) -> list:
    l_i = 0
    r_i = len(seq)
    return _quicksort(seq.copy(), l_i, r_i)


def _quicksort(seq: list, l_i: int, r_i: int) -> list:
    if r_i - l_i < 1:
        return seq
    p_i = choose_pivot(l_i, r_i)
    seq, p_i = partition(seq, l_i, r_i, p_i)
    seq = _quicksort(seq, l_i, p_i)
    seq = _quicksort(seq, p_i + 1, r_i)
    return seq


def choose_pivot(l_i: int, r_i: int) -> int:
    return random.randint(l_i, r_i - 1)


def choose_pivot_exercise(l_i: int, r_i: int) -> int:
    return l_i


def partition(seq: list, l_i: int, r_i: int, p_i: int) -> Tuple[list, int]:
    """Partition a part of the given sequence.

    Choose an item `p` to partition by and move all items `x < p` to the left of `p`
    and all items `x > p` to the right of `p`.
    :param seq: The sequence to partition.
    :param l_i: The leftmost index.
    :param r_i: The rightmost index.
    :param p_i: Partition index.
    :returns: A tuple of:
        * Same sequence with the part bounded by `l_i` and `r_i` partitioned;
        * The new index of the partition element.
    """
    # Lets start by moving the partition key to the front of the sequence.
    # Just so it's easier to keep track of it as items get moved around.
    seq[p_i], seq[l_i] = seq[l_i], seq[p_i]
    p = seq[l_i]
    p_i = l_i
    i = p_i + 1
    for j in range(i, r_i):
        if seq[j] > p:
            continue
        temp = seq[i]
        seq[i] = seq[j]
        seq[j] = temp
        i += 1
    p_i_new = i - 1
    seq[p_i] = seq[p_i_new]
    seq[p_i_new] = p
    return seq, p_i_new
