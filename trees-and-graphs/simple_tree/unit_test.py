import unittest
from .simple_tree import SimpleTreeNode, SimpleTree


class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        self.root = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.root)
        self.child1 = SimpleTreeNode(2, self.root)
        self.child2 = SimpleTreeNode(3, self.root)
        self.tree.AddChild(self.root, self.child1)
        self.tree.AddChild(self.root, self.child2)
        self.grandchild1 = SimpleTreeNode(4, self.child1)
        self.tree.AddChild(self.child1, self.grandchild1)

    def test_AddChild(self):
        self.assertIn(self.child1, self.root.Children)
        self.assertEqual(self.child1.Parent, self.root)
        self.assertEqual(self.child1.Level, 1)

    def test_DeleteNode(self):
        self.tree.DeleteNode(self.child1)
        self.assertNotIn(self.child1, self.root.Children)
        self.assertIsNone(self.child1.Parent)

    def test_GetAllNodes(self):
        nodes = self.tree.GetAllNodes()
        self.assertEqual(len(nodes), 4)
        self.assertIn(self.child1, nodes)
        self.assertIn(self.child2, nodes)
        self.assertIn(self.grandchild1, nodes)

    def test_FindNodesByValue(self):
        found_nodes = self.tree.FindNodesByValue(2)
        self.assertEqual(len(found_nodes), 1)
        self.assertEqual(found_nodes[0], self.child1)

    def test_MoveNode(self):
        self.tree.MoveNode(self.grandchild1, self.child2)
        self.assertIn(self.grandchild1, self.child2.Children)
        self.assertNotIn(self.grandchild1, self.child1.Children)
        self.assertEqual(self.grandchild1.Parent, self.child2)

    def test_Count(self):
        count = self.tree.Count()
        self.assertEqual(count, 4)

    def test_LeafCount(self):
        leaf_count = self.tree.LeafCount()
        self.assertEqual(leaf_count, 2)  # After setup, child2 and grandchild1 are leaves


if __name__ == "__main__":
    unittest.main()
