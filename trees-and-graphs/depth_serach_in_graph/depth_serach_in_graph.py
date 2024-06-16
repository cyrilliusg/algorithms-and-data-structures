from typing import Optional


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency: list[list[int]] = [[0] * size for _ in range(size)]
        self.vertex: list[Optional[Vertex]] = [None] * size

    def AddVertex(self, v: int) -> None:
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return

    def RemoveVertex(self, v: int) -> None:
        if self.vertex[v] is None:
            self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if self.vertex[v1] is None or self.vertex[v2] is None:
            self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if self.vertex[v1] is None or self.vertex[v2] is None:
            self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list[Vertex]:
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

        stack = []
        path = []
        self._dfs_recursive(VFrom, VTo, stack, path)
        return path

    def _dfs_recursive(self, current: int, target: int, stack: list[int], path: list[Vertex]) -> bool:
        self.vertex[current].Hit = True
        stack.append(current)

        if current == target:
            for index in stack:
                path.append(self.vertex[index])
            return True

        for neighbor in range(self.max_vertex):
            if self.m_adjacency[neighbor][current] == 1 and not self.vertex[neighbor].Hit:
                if self._dfs_recursive(neighbor, target, stack, path):
                    return True

        stack.pop()
        return False

