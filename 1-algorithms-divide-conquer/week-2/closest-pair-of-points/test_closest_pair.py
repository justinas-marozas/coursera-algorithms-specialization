from typing import List, Tuple

import nose

from parameterized import parameterized

import closest_pair


Point = Tuple[float, float]

POINTS_1: List[Point] = [
    (73.24, 43.09),
    (7.19, 92.69),
    (79.91, 13.63),
    (51.94, 124.1),
    (102.97, 27.57),
    (21.52, 96.38)
]
CLOSEST_DISTANCE_1 = 14.797
CLOSEST_PAIR_1: List[Point] = [
    (7.19, 92.69),
    (21.52, 96.38)
]


@parameterized([
    (POINTS_1, CLOSEST_DISTANCE_1),
])
def test_closest_pair_distance_computed_correctly(points: List[Point], expected: float) -> None:
    _, actual = closest_pair.find_closest_pair(points)

    assert round(actual, 3) == round(expected, 3)


@parameterized([
    (POINTS_1, CLOSEST_PAIR_1),
])
def test_correct_closest_pair_found(points: List[Point], expected: List[Point]) -> None:
    actual, _ = closest_pair.find_closest_pair(points)

    assert actual == expected


if __name__ == '__main__':
    nose.main()
