import math
from typing import List, NamedTuple, Tuple


class Point(NamedTuple):
    x: float
    y: float


def find_closest_pair(points: List[Point]) -> Tuple[List[Point], float]:
    sorted_points = sort_points(points)
    best_pair = sorted_points[:2]
    best_dist = get_distance(*best_pair)
    return recursive(sorted_points, best_pair, best_dist)


def recursive(
    points: List[Point],
    best_pair: List[Point],
    best_distance: float
) -> Tuple[List[Point], float]:
    if len(points) < 2:
        return best_pair, best_distance
    if len(points) == 2:
        return points, get_distance(*points)
    points_a, points_b = split(points)
    best_pair_a, best_dist_a = recursive(points_a, best_pair, best_distance)
    best_pair_b, best_dist_b = recursive(points_b, best_pair, best_distance)
    best_pair, best_dist = min([
        (best_pair_a, best_dist_a),
        (best_pair_b, best_dist_b),
        (best_pair, best_distance)
    ], key=lambda x: x[1])
    return find_closest_split_pair(points_a, points_b, best_pair, best_dist)


def naive(points: List[Point]) -> Tuple[List[Point], float]:
    best_pair = points[:2]
    best_dist = get_distance(*best_pair)
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            dist = get_distance(points[i], points[j])
            if dist < best_dist:
                best_dist = dist
                best_pair = [points[i], points[j]]
    return best_pair, best_dist


def get_distance(a: Point, b: Point) -> float:
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5


def sort_points(points: List[Point]) -> List[Point]:
    sorted_x = sorted(points, key=lambda p: p.x)
    sorted_yx = sorted(sorted_x, key=lambda p: p.y)
    return sorted_yx


def split(points: List[Point]) -> Tuple[List[Point], List[Point]]:
    split_point = math.ceil(len(points) / 2)
    return points[:split_point], points[split_point:]


def find_closest_split_pair(
    points_a: List[Point],
    points_b: List[Point],
    best_pair: List[Point],
    best_distance: float
) -> Tuple[List[Point], float]:
    candidates = find_potential_split_pairs(points_a, points_b, best_distance)
    for i, _ in enumerate(candidates):
        for j in range(i + 1, min(i + 7, len(candidates))):
            dist = get_distance(candidates[i], candidates[j])
            if dist < best_distance:
                best_distance = dist
                best_pair = [candidates[i], candidates[j]]
    return best_pair, best_distance


def find_potential_split_pairs(
    points_a: List[Point],
    points_b: List[Point],
    best_distance: float
) -> List[Point]:
    x_division = max(points_a, key=lambda p: p.x).x
    return [
        point
        for point in points_a
        if point.x > x_division - best_distance
    ] + [
        point
        for point in points_b
        if point.x < x_division + best_distance
    ]
