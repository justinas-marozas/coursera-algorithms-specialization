import math
from typing import List, Tuple


def merge_sort(seq: List) -> List:
    if len(seq) == 1:
        return seq
    sub_a, sub_b = split(seq)
    sub_a_sorted = merge_sort(sub_a)
    sub_b_sorted = merge_sort(sub_b)
    return merge(sub_a_sorted, sub_b_sorted)


def split(seq: List) -> Tuple[List, List]:
    len_a = math.ceil(len(seq) / 2)
    return seq[:len_a], seq[len_a:]


def merge(seq_a: List, seq_b: List) -> List:
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
            if i_b == len(seq_b):
                merged.extend(seq_a[i_a:])
                break
    return merged
