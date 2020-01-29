from typing import List


def partition(seq: List, l_i: int, r_i: int) -> List:
    """Partition a part of the given sequence.

    Choose an item `p` to partition by and move all items `x < p` to the left of `p`
    and all items `x > p` to the right of `p`.
    :param seq: The sequence to partition.
    :param l_i: The leftmost index.
    :param r_i: The rightmost index.
    :returns: Same sequence with the part bounded by `l_i` and `r_i` partitioned.
    """
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
    seq[p_i] = seq[i - 1]
    seq[i - 1] = p
    return seq
