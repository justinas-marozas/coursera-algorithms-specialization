import math
from typing import List, Tuple, TypeVar


T = TypeVar('T', int, float)


def d_select(seq: List[T], order: int) -> T:
    print(f'{seq = }; {order = };')
    ith = order - 1
    l_i = 0
    r_i = len(seq) - 1
    ith_order_el = _d_select(seq.copy(), ith, l_i, r_i)
    return ith_order_el


def _d_select(seq: List[T], ith: int, l_i: int, r_i: int) -> T:
    print(f'{seq = }; {ith = }; {l_i = }; {r_i = };')
    if len(seq[l_i:r_i + 1]) <= 1:
        return seq[l_i]
    p_i = pick_pivot(seq, l_i, r_i)
    print(f'{p_i = };')
    seq, p_i = partition(seq, l_i, r_i, p_i)
    print(f'{p_i = };')
    if p_i == ith:
        return seq[p_i]
    if p_i > ith:
        return _d_select(seq, ith, l_i, p_i - 1)
    return _d_select(seq, ith, p_i + 1, r_i)


def pick_pivot(seq: List[T], l_i: int, r_i: int) -> int:
    median_idx, _ = median_of_medians(seq, l_i, r_i)
    return median_idx


def median_of_medians(seq: List[T], l_i: int, r_i: int) -> Tuple[int, T]:
    slices = [
        list(enumerate(seq[i:i + 5 if i + 5 <= r_i else r_i], i))
        for i in range(l_i, r_i, 5)
    ]
    medians = [
        get_median(s)
        for s in slices
    ]
    return get_median(medians)


def get_median(seq: List[Tuple[int, T]]) -> Tuple[int, T]:
    median_idx = math.floor(len(seq) / 2)
    sorted_seq = sorted(seq, key=lambda x: x[1])
    return sorted_seq[median_idx]


def partition(seq: List[T], l_i: int, r_i: int, p_i: int) -> Tuple[List[T], int]:
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
    for j in range(i, r_i + 1):
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
