import unittest
from .breadth_serach_in_graph import SimpleGraph


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

    def test_path_exists(self):
        path = self.graph.DepthFirstSearch(0, 4)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1, 3, 4])

    def test_no_path(self):
        self.graph.RemoveEdge(3, 4)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [])

    def test_same_start_and_end(self):
        path = self.graph.DepthFirstSearch(0, 0)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0])

    def test_direct_connection(self):
        path = self.graph.DepthFirstSearch(0, 1)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1])

    def test_complex_path(self):
        self.graph.AddEdge(1, 4)

        path = self.graph.DepthFirstSearch(0, 4)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1, 3, 4])  # best path should be [0, 1, 4]

    def test_bfs_path_exists(self):
        path = self.graph.BreadthFirstSearch(0, 4)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1, 3, 4])

    def test_bfs_no_path(self):
        self.graph.RemoveEdge(3, 4)
        path = self.graph.BreadthFirstSearch(0, 4)
        self.assertEqual(path, [])

    def test_bfs_same_start_and_end(self):
        path = self.graph.BreadthFirstSearch(0, 0)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0])

    def test_bfs_direct_connection(self):
        path = self.graph.BreadthFirstSearch(0, 1)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1])

    def test_bfs_complex_path(self):
        self.graph.AddEdge(1, 4)
        path = self.graph.BreadthFirstSearch(0, 4)
        result = [vertex.Value for vertex in path]
        self.assertEqual(result, [0, 1, 4])


if __name__ == '__main__':
    unittest.main()
