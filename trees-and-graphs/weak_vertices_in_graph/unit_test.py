import unittest
from .weak_vertices_in_graph import SimpleGraph


class TestSimpleGraph(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(5)
        for i in range(5):
            self.graph.AddVertex(i)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)

    def test_weak_vertices_with_strong(self):
        self.graph.AddEdge(1, 2)
        weak_vertices = self.graph.WeakVertices()
        result = [vertex.Value for vertex in weak_vertices]
        self.assertEqual(result, [4])

    def test_weak_vertices_without_strong(self):
        weak_vertices = self.graph.WeakVertices()
        result = [vertex.Value for vertex in weak_vertices]
        self.assertEqual(result, [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
