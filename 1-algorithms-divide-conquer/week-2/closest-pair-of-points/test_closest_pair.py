from typing import List

import nose
import numpy as np
from parameterized import parameterized
from scipy import spatial

import closest_pair
from closest_pair import Point


# Closest pair is in one of the recursion divisions.
POINTS_1: List[Point] = [
    Point(x=73.24, y=43.09),
    Point(x=7.19, y=92.69),
    Point(x=79.91, y=13.63),
    Point(x=51.94, y=124.1),
    Point(x=102.97, y=27.57),
    Point(x=21.52, y=96.38)
]
CLOSEST_PAIR_1: List[Point] = [
    Point(x=7.19, y=92.69),
    Point(x=21.52, y=96.38)
]
CLOSEST_DISTANCE_1 = 14.797465999

# Closest pair is split between multiple recursion divisions.
POINTS_2: List[Point] = [
    Point(x=91.05, y=47.1),
    Point(x=52.28, y=74.25),
    Point(x=51.45, y=82.87),
    Point(x=88.68, y=112.45),
    Point(x=52.18, y=96.39),
    Point(x=19.59, y=89.68),
    Point(x=97.95, y=115.67),
    Point(x=83.82, y=65.75),
    Point(x=99.89, y=52.11),
    Point(x=1.71, y=98.47),
    Point(x=44.53, y=120.39),
    Point(x=89.8, y=30.52),
    Point(x=44.58, y=71.62),
    Point(x=105.48, y=95.92),
    Point(x=103.84, y=70.26)
]
CLOSEST_PAIR_2: List[Point] = [
    Point(x=52.28, y=74.25),
    Point(x=44.58, y=71.62)
]
CLOSEST_DISTANCE_2 = 8.13676


@parameterized([
    (POINTS_1, CLOSEST_DISTANCE_1),
    (POINTS_2, CLOSEST_DISTANCE_2)
])
def test_closest_pair_distance_computed_correctly(points: List[Point], expected: float) -> None:
    _, actual = closest_pair.find_closest_pair(points)

    assert round(actual, 3) == round(expected, 3)


@parameterized([
    (POINTS_1, CLOSEST_PAIR_1),
    (POINTS_2, CLOSEST_PAIR_2)
])
def test_correct_closest_pair_found(points: List[Point], expected: List[Point]) -> None:
    actual, _ = closest_pair.find_closest_pair(points)

    assert (actual == expected) or (list(reversed(actual)) == expected)


def test_with_large_random_input() -> None:
    points_np = np.random.uniform(-128., 128., size=(3333, 2))
    dist_matrix = spatial.distance_matrix(points_np, points_np)
    expected_dist = dist_matrix[dist_matrix > 0.].min()
    point_a_idx, point_b_idx = np.where(dist_matrix == expected_dist)[0]
    points = [
        Point(x=point[0], y=point[1])
        for point in points_np
    ]
    expected_pair = [points[point_a_idx], points[point_b_idx]]

    actual_pair, actual_dist = closest_pair.find_closest_pair(points)

    assert (actual_pair == expected_pair) or (list(reversed(actual_pair)) == expected_pair)
    assert round(actual_dist, 3) == round(expected_dist, 3)


if __name__ == '__main__':
    nose.main()
