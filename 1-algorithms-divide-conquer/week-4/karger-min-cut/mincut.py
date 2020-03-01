import random
from typing import Generator, List, Tuple


RawVertex = Tuple[int, List[int]]
Edge = Tuple[int, int]


def main() -> None:
    vertices = read_file('vertices.txt')
    edges = convert_to_edges(vertices)
    graph = list(edges)
    min_cuts = estimate_min_cut(graph)
    print(min_cuts)


def read_file(filepath: str) -> Generator[RawVertex, None, None]:
    for line in open(filepath, mode='r', encoding='utf-8'):
        line = line.strip()
        vertices = [
            int(label)
            for label in line.split('\t')
        ]
        yield vertices[0], vertices[1:]


def convert_to_edges(vertices: Generator[RawVertex, None, None]) -> Generator[Edge, None, None]:
    for vertex in vertices:
        yield from vertex_to_edge(vertex)


def vertex_to_edge(vertex: RawVertex) -> Generator[Edge, None, None]:
    u, vs = vertex
    for v in vs:
        yield u, v


def random_contraction(graph: List[Edge]) -> List[Edge]:
    """
    While there are more than 2 vertices:
    * Pick a random edge;
    * Merge vertices of the picked edge;
    * Remove self-loops;
    """
    while count_vertices(graph) > 2:
        pivot = random.choice(graph)
        graph = merge_vertices(graph, pivot)
        graph = remove_self_loops(graph)
    return graph


def count_vertices(graph: List[Edge]) -> int:
    labels = set()
    for u, v in graph:
        labels.add(u)
        labels.add(v)
    return len(labels)


def merge_vertices(graph: List[Edge], pivot: Edge) -> List[Edge]:
    new_label = min(pivot)
    for i, edge in enumerate(graph):
        u, v = edge
        if u in pivot:
            u = new_label
        if v in pivot:
            v = new_label
        if (u, v) != edge:
            graph[i] = (u, v)
    return graph


def remove_self_loops(graph: List[Edge]) -> List[Edge]:
    return [
        (u, v)
        for u, v in graph
        if u != v
    ]


def estimate_min_cut(graph: List[Edge]) -> int:
    cuts = [
        random_contraction(graph)
        for _ in range(count_vertices(graph))
    ]
    lengths = [len(cut) for cut in cuts]
    return min(lengths)


if __name__ == '__main__':
    main()
