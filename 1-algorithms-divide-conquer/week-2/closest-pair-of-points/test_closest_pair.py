from typing import List

import nose

from parameterized import parameterized

import closest_pair
from closest_pair import Point


POINTS_1: List[Point] = [
    Point(x=73.24, y=43.09),
    Point(x=7.19, y=92.69),
    Point(x=79.91, y=13.63),
    Point(x=51.94, y=124.1),
    Point(x=102.97, y=27.57),
    Point(x=21.52, y=96.38)
]
CLOSEST_DISTANCE_1 = 14.797
CLOSEST_PAIR_1: List[Point] = [
    Point(x=7.19, y=92.69),
    Point(x=21.52, y=96.38)
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
