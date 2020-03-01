import math
from typing import List, Tuple, TypeVar


T = TypeVar('T', int, float)


def r_select(seq: List[T], order: int) -> T:
    print(f'{seq = }; {order = };')
    ith = order - 1
    l_i = 0
    r_i = len(seq) - 1
    ith_order_el = _r_select(seq.copy(), ith, l_i, r_i)
    return ith_order_el


def _r_select(seq: List[T], ith: int, l_i: int, r_i: int) -> T:
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
        return _r_select(seq, ith, l_i, p_i - 1)
    # ith -= p_i
    return _r_select(seq, ith, p_i + 1, r_i)


def pick_pivot(seq: List[T], l_i: int, r_i: int) -> int:
    """Pick an index of a three-reference-point median as a pivot.

    Pick a median from leftmost, rightmost and middle points in the given window.
    """
    l_val = seq[l_i]
    r_val = seq[r_i]
    m_i = math.floor((r_i - l_i) / 2) + l_i
    m_val = seq[m_i]
    sorted_points = sorted(
        [
            (l_i, l_val),
            (m_i, m_val),
            (r_i, r_val)
        ],
        key=lambda x: x[1]
    )
    median_i, _ = sorted_points[1]
    return median_i


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
