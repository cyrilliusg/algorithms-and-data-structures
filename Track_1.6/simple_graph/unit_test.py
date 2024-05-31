import unittest

from .simple_graph import SimpleGraph


class TestSimpleGraph(unittest.TestCase):
    def test_add_vertex(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        self.assertIsNotNone(graph.vertex[0])
        self.assertEqual(graph.vertex[0].Value, 1)
        for i in range(graph.max_vertex):
            self.assertEqual(sum(graph.m_adjacency[i]), 0)

    def test_add_edge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        self.assertFalse(graph.IsEdge(0, 1))
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 0))

    def test_remove_edge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))
        graph.RemoveEdge(0, 1)
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))

    def test_remove_vertex(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))
        graph.RemoveVertex(0)
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(0, 2))
        self.assertFalse(graph.IsEdge(1, 0))
        self.assertFalse(graph.IsEdge(2, 0))
        self.assertIsNone(graph.vertex[0])


if __name__ == '__main__':
    unittest.main()
