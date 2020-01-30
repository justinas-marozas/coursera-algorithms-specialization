

def partition(seq: list, l_i: int, r_i: int, p_i: int) -> list:
    """Partition a part of the given sequence.

    Choose an item `p` to partition by and move all items `x < p` to the left of `p`
    and all items `x > p` to the right of `p`.
    :param seq: The sequence to partition.
    :param l_i: The leftmost index.
    :param r_i: The rightmost index.
    :param p_i: Partition index.
    :returns: Same sequence with the part bounded by `l_i` and `r_i` partitioned.
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
    seq[p_i] = seq[i - 1]
    seq[i - 1] = p
    return seq
