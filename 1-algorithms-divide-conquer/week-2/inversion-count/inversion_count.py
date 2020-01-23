import math
from typing import List, Tuple


def count_inversions(seq: List) -> Tuple[int, List]:
    if len(seq) == 1:
        return (0, seq)
    sub_a, sub_b = split(seq)
    (count_a, sub_a_sorted) = count_inversions(sub_a)
    (count_b, sub_b_sorted) = count_inversions(sub_b)
    count = count_a + count_b
    return merge_and_count(sub_a_sorted, sub_b_sorted, count)


def split(seq: List) -> Tuple[List, List]:
    len_a = math.ceil(len(seq) / 2)
    return seq[:len_a], seq[len_a:]


def merge_and_count(seq_a: List, seq_b: List, count: int) -> Tuple[int, List]:
    total_len = len(seq_a) + len(seq_b)
    merged = []
    i_a = 0
    i_b = 0
    for _ in range(total_len):
        if seq_a[i_a] < seq_b[i_b]:
            merged.append(seq_a[i_a])
            i_a += 1
            if i_a == len(seq_a):
                merged.extend(seq_b[i_b:])
                break
        else:
            merged.append(seq_b[i_b])
            i_b += 1
            count += len(seq_a[i_a:])
            if i_b == len(seq_b):
                merged.extend(seq_a[i_a:])
                break
    return (count, merged)
