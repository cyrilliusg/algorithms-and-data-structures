class Vertex:
    def __init__(self, val):
        self.Value = val


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # добавление новой вершины со значением value в свободное место массива vertex
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return
        raise Exception("Graph is full, cannot add more vertices")

    def RemoveVertex(self, v):
        # удаление вершины со всеми её рёбрами
        if self.vertex[v] is None:
            raise Exception("Vertex not found")
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.vertex[v1] is None or self.vertex[v2] is None:
            raise Exception("One or both vertices not found")
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.vertex[v1] is None or self.vertex[v2] is None:
            raise Exception("One or both vertices not found")
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0


if __name__ == '__main__':
    graph = SimpleGraph(3)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    print(graph.m_adjacency)
