from typing import List

import pytest

import mincut


@pytest.fixture
def graph() -> List[mincut.Edge]:
    return [
        (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 5), (2, 7),
        (3, 1), (3, 4),
        (4, 1), (4, 3), (4, 5), (4, 6), (4, 7),
        (5, 2), (5, 4), (5, 7),
        (6, 4), (6, 7), (6, 8),
        (7, 2), (7, 4), (7, 5), (7, 6), (7, 8),
        (8, 6), (8, 7),
    ]


@pytest.fixture
def vertices() -> List[mincut.RawVertex]:
    return [
        (1, [2, 3, 4]),
        (2, [1, 5, 7]),
        (3, [1, 4]),
        (4, [1, 3, 5, 6, 7]),
        (5, [2, 4, 7]),
        (6, [4, 7, 8]),
        (7, [2, 4, 5, 6, 8]),
        (8, [6, 7]),
    ]


class TestReadFile:

    @pytest.fixture
    def file_mock(self, mocker):
        fn = mocker.patch.object(mincut, 'open')
        fn.return_value = (
            '\t'.join(str(x) for x in range(i, 5, -1))
            for i in range(10, 50)
        )
        return fn

    @pytest.fixture
    def actual(self, file_mock) -> List[mincut.RawVertex]:
        return list(mincut.read_file('asd'))

    def test_expected_structure_is_returned(self, actual: List[mincut.RawVertex]) -> None:
        for u, vs in actual:
            assert isinstance(u, int)
            assert isinstance(vs, list)

    def test_expected_values_are_returned(self, actual: List[mincut.RawVertex]) -> None:
        expected = [
            (i, list(range(i - 1, 5, -1)))
            for i in range(10, 50)
        ]
        for (exp_u, exp_vs), (act_u, act_vs) in zip(expected, actual):
            assert act_u == exp_u
            assert act_vs == exp_vs


class TestConvertToEdges:

    def test_vertices_converted_to_correct_edges(self, vertices, graph) -> None:
        expected = graph
        actual = mincut.convert_to_edges(vertices)
        actual = list(actual)
        assert set(actual) == set(expected)


class TestCountVertices:

    def test_vertices_are_counted_correctly(self, graph) -> None:
        actual = mincut.count_vertices(graph)
        assert actual == 8


class TestRemoveSelfLoops:

    def test_self_loops_removed(self) -> None:
        graph = [
            (1, 2), (1, 1), (1, 3), (1, 4),
            (2, 1), (2, 5), (2, 2), (2, 7),
            (3, 1), (3, 4), (3, 3),
        ]
        expected = [
            (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 5), (2, 7),
            (3, 1), (3, 4),
        ]
        actual = mincut.remove_self_loops(graph)
        assert actual == expected


class TestContractVertices:

    def test_pivot_edges_get_merged(self, graph) -> None:
        pivot = (3, 1)
        expected = [
            (1, 2), (1, 1), (1, 4),
            (2, 1), (2, 5), (2, 7),
            (1, 1), (1, 4),
            (4, 1), (4, 1), (4, 5), (4, 6), (4, 7),
            (5, 2), (5, 4), (5, 7),
            (6, 4), (6, 7), (6, 8),
            (7, 2), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 6), (8, 7),
        ]

        actual = mincut.merge_vertices(graph, pivot)

        assert set(actual) == set(expected)


class TestRandomContraction:

    @pytest.fixture
    def actual(self, graph) -> List[mincut.Edge]:
        return mincut.random_contraction(graph)

    def test_two_vertices_remain(self, actual) -> None:
        assert mincut.count_vertices(actual) == 2

    def test_no_self_references_remain(self, actual) -> None:
        assert all(u != v for u, v in actual)


class TestEstimateMinCuts:

    @pytest.mark.xfail(reason='The algorithm is random and approximate.')
    def test_it(self, graph) -> None:
        actual = mincut.estimate_min_cut(graph)
        assert actual == 4
