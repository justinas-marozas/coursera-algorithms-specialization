import random
from typing import List, NamedTuple, Tuple

import numpy as np
import pytest
from _pytest.fixtures import SubRequest

import dselect


class PartitionParams(NamedTuple):
    seq: list
    l_i: int
    r_i: int
    p_i: int
    p_i_expected: int


class DSelectParams(NamedTuple):
    seq: List[int]
    order: int
    expected: int


class TestPartition:

    @pytest.fixture(
        scope='class',
        params=[
            # Basic examples:
            PartitionParams([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 0, 2),
            PartitionParams([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 4, 0),
            PartitionParams([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 1, 7),
            # Go through sorting steps:
            PartitionParams([3, 8, 2, 5, 1, 4, 7, 6], 0, 7, 3, 4),
            PartitionParams([4, 2, 3, 1, 5, 8, 7, 6], 0, 5, 2, 2),
            PartitionParams([1, 2, 3, 4, 5, 8, 7, 6], 5, 7, 7, 5),
            PartitionParams([1, 2, 3, 4, 5, 6, 7, 8], 0, 2, 1, 1),
            PartitionParams([1, 2, 3, 4, 5, 6, 7, 8], 6, 7, 6, 6),
        ],
        ids=[
            # Basic examples:
            'partition middle',
            'partition leftmost',
            'partition rightmost',
            # Go through sorting, steps:
            'sort step 1',
            'sort step 2',
            'sort step 3',
            'sort step 4',
            'sort step 5',
        ]
    )
    def partition_params(self, request: SubRequest) -> PartitionParams:
        return request.param

    @pytest.fixture(scope='class')
    def partition_result(self, partition_params: PartitionParams) -> Tuple[list, int]:
        seq, l_i, r_i, p_i, _ = partition_params
        return dselect.partition(seq.copy(), l_i, r_i, p_i)

    def test_pivot_moved_to_correct_index(
        self,
        partition_params: PartitionParams,
        partition_result: Tuple[list, int]
    ) -> None:
        """Verify partition step works."""
        _, _, _, _, p_i_expected = partition_params
        _, p_i_actual = partition_result

        assert p_i_actual == p_i_expected

    def test_pivot_has_correct_value(
        self,
        partition_params: PartitionParams,
        partition_result: Tuple[list, int]
    ) -> None:
        """Verify partition step works."""
        seq, _, _, p_i, _ = partition_params
        seq_actual, p_i_actual = partition_result
        pivot = seq[p_i]

        assert seq_actual[p_i_actual] == pivot

    def test_all_items_left_to_pivot_are_smaller(self, partition_result: Tuple[list, int]) -> None:
        """Verify partition step works."""
        seq_actual, p_i_actual = partition_result

        assert all(
            x < seq_actual[p_i_actual]
            for x in seq_actual[:p_i_actual]
        )

    def test_all_items_right_to_pivot_are_larger(self, partition_result: Tuple[list, int]) -> None:
        """Verify partition step works."""
        seq_actual, p_i_actual = partition_result
        assert all(
            x > seq_actual[p_i_actual]
            for x in seq_actual[p_i_actual + 1:]
        )


def expand_d_select_params(seq: list) -> List[DSelectParams]:
    return [
        DSelectParams(seq, i, x)
        for i, x in enumerate(sorted(seq), 1)
    ]


class TestMedianOfMedians:

    @pytest.fixture(
        scope='class',
        params=[
            np.random.choice(range(0, 125), size=125, replace=False).tolist(),
            np.random.choice(range(159, 354), size=195, replace=False).tolist(),
            np.random.choice(range(24, 77), size=53, replace=False).tolist(),
        ]
    )
    def params(self, request: SubRequest) -> List[int]:
        return request.param

    @pytest.fixture(scope='class')
    def sub_range(self, params: List[int]) -> Tuple[int, int]:
        seq = params
        l_i = np.random.randint(0, len(seq) * 0.2)
        r_i = np.random.randint(len(seq) * 0.8, len(seq) - 1)
        return l_i, r_i

    def test_entire_sequence_median(self, params: List[int]) -> None:
        seq = params
        n = len(seq)
        _, actual_median = dselect.median_of_medians(seq, 0, n - 1)

        assert np.percentile(seq, 40) < actual_median < np.percentile(seq, 60)

    def test_subsequence_median(self, params: List[int], sub_range: Tuple[int, int]) -> None:
        seq = params
        l_i, r_i = sub_range
        sub_seq = seq[l_i:r_i + 1]
        _, actual_median = dselect.median_of_medians(seq, l_i, r_i)

        assert np.percentile(sub_seq, 40) < actual_median < np.percentile(sub_seq, 60)

    def test_subsequence_index(self, params: List[int], sub_range: Tuple[int, int]) -> None:
        seq = params
        l_i, r_i = sub_range
        actual_idx, _ = dselect.median_of_medians(seq, l_i, r_i)

        assert l_i <= actual_idx <= r_i


class TestDSelect:

    @pytest.fixture(
        scope='class',
        params=(
            expand_d_select_params(random.sample(range(20), 20))
            + expand_d_select_params(random.sample(range(100, 201), 101))
        ),
        ids=(
            [
                f'{i}th order from 0-19'
                for i, n in enumerate(range(20), 1)
            ] + [
                f'{i}th order from 100-200'
                for i, n in enumerate(range(100, 201), 1)
            ]
        )
    )
    def d_select_params(self, request: SubRequest) -> DSelectParams:
        return request.param

    def test_d_select_picks_correct_element(self, d_select_params: DSelectParams) -> None:
        actual = dselect.d_select(d_select_params.seq, d_select_params.order)
        assert actual == d_select_params.expected

    def test_input_sequence_was_not_modified(self) -> None:
        seq = random.sample(range(100), 100)
        expected = seq.copy()
        n = random.randint(0, 100)

        _ = dselect.d_select(seq, n)

        assert seq == expected
