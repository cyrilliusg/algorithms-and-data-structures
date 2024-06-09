import unittest
from .forests import SimpleTreeNode, SimpleTree


class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        root = SimpleTreeNode(1, None)
        self.tree = SimpleTree(root)

        node2 = SimpleTreeNode(2, root)
        node3 = SimpleTreeNode(3, root)
        node6 = SimpleTreeNode(6, root)
        self.tree.AddChild(root, node2)
        self.tree.AddChild(root, node3)
        self.tree.AddChild(root, node6)

        node5 = SimpleTreeNode(5, node2)
        node7 = SimpleTreeNode(7, node2)
        self.tree.AddChild(node2, node5)
        self.tree.AddChild(node2, node7)

        node4 = SimpleTreeNode(4, node3)
        self.tree.AddChild(node3, node4)

        node8 = SimpleTreeNode(8, node6)
        self.tree.AddChild(node6, node8)

        node9 = SimpleTreeNode(9, node8)
        node10 = SimpleTreeNode(10, node8)
        self.tree.AddChild(node8, node9)
        self.tree.AddChild(node8, node10)

    def test_even_trees(self):
        result = self.tree.EvenTrees()
        result_values = [node.NodeValue for node in result]
        expected_values = [1, 3, 1, 6]

        self.assertEqual(result_values, expected_values)

    def test_even_trees_no_removal(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        result = tree.EvenTrees()
        self.assertEqual(result, [])

    def test_even_trees_single_child(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        node2 = SimpleTreeNode(2, root)
        tree.AddChild(root, node2)
        result = tree.EvenTrees()
        self.assertEqual(result, [])

    def test_even_trees_multiple_levels(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)

        node2 = SimpleTreeNode(2, root)
        node3 = SimpleTreeNode(3, root)
        tree.AddChild(root, node2)
        tree.AddChild(root, node3)

        node4 = SimpleTreeNode(4, node2)
        node5 = SimpleTreeNode(5, node2)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, node3)
        tree.AddChild(node3, node6)

        node7 = SimpleTreeNode(7, node4)
        tree.AddChild(node4, node7)

        result = tree.EvenTrees()
        result_values = [node.NodeValue for node in result]
        expected_values = [1, 2, 1, 3, 2, 4]

        self.assertEqual(result_values, expected_values)


if __name__ == "__main__":
    unittest.main()
