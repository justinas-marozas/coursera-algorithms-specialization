from typing import List, NamedTuple, Tuple


class Point(NamedTuple):
    x: float
    y: float


def find_closest_pair(points: List[Point]) -> Tuple[List[Point], float]:
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
