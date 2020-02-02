import math
import random
from typing import Callable, Tuple


def quicksort(seq: list) -> list:
    """Sort the given sequence using a QuickSort algorithm."""
    l_i = 0
    r_i = len(seq)
    sorted_seq, _ = _quicksort(seq.copy(), l_i, r_i)
    return sorted_seq


def pick_random(seq: list, l_i: int, r_i: int) -> int:
    """Pick a random index as a pivot."""
    return random.randint(l_i, r_i - 1)


def pick_leftmost(seq: list, l_i: int, r_i: int) -> int:
    """Pick a leftmost index as a pivot."""
    return l_i


def pick_rightmost(seq: list, l_i: int, r_i: int) -> int:
    """Pick a rightmost index as a pivot."""
    return r_i - 1


def pick_median_from_left_mid_right_points(seq: list, l_i: int, r_i: int) -> int:
    """Pick an index of a three-reference-point median as a pivot.

    Pick a median from leftmost, rightmost and middle points in the given window.
    """
    r_i -= 1
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


def _quicksort(
    seq: list,
    l_i: int,
    r_i: int,
    pivot_picker: Callable[[list, int, int], int] = pick_random,
    n_comparisons: int = 0,
) -> Tuple[list, int]:
    """QuickSort algorithm.

    1. Use given `pivot_picker` function to pick a pivot point in the `seq`;
    2. Partition the `seq` window bound by `l_i` and `r_i` by separating all values
        lower than the pivot from the greater ones;
    3. Recursively use QuickSort algorithm on both partitions;
    4. Return the sorted `seq`.
    :param seq: A sequence to be sorted.
    :param l_i: A leftmost index to bound current QuickSort iteration by.
    :param r_i: A rightmost index to bound current QuickSort iteration by.
    :param pivot_picker: A function to use to pick a pivot point.
    :param n_comparisons: A cumulative sum of all comparisons done by the algorithm so far.
        Only used for assignments.
    :returns: A `seq` with the window bounded by `l_i` and `r_i` is sorted.
    """
    if r_i - l_i < 1:
        return seq, n_comparisons
    p_i = pivot_picker(seq, l_i, r_i)
    n_comparisons += r_i - l_i - 1
    seq, p_i = partition(seq, l_i, r_i, p_i)
    seq, n_comparisons = _quicksort(seq, l_i, p_i, pivot_picker, n_comparisons)
    seq, n_comparisons = _quicksort(seq, p_i + 1, r_i, pivot_picker, n_comparisons)
    return seq, n_comparisons


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


def quicksort_assignment_1(seq: list) -> Tuple[list, int]:
    """Count the number of comparisons when using leftmost item as partition."""
    l_i = 0
    r_i = len(seq)
    return _quicksort(seq.copy(), l_i, r_i, pick_leftmost)


def quicksort_assignment_2(seq: list) -> Tuple[list, int]:
    """Count the number of comparisons when using rightmost item as partition."""
    l_i = 0
    r_i = len(seq)
    return _quicksort(seq.copy(), l_i, r_i, pick_rightmost)


def quicksort_assignment_3(seq: list) -> Tuple[list, int]:
    """Count the number of comparisons when using median of [leftmost, mid, rightmost] items as partition."""
    l_i = 0
    r_i = len(seq)
    return _quicksort(seq.copy(), l_i, r_i, pick_median_from_left_mid_right_points)
