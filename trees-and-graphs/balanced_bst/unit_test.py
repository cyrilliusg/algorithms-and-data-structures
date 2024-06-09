from .balanced_bst import BalancedBST, BSTNode
import unittest


class TestBalancedBST(unittest.TestCase):

    def setUp(self):
        self.bst = BalancedBST()

    def test_empty_array(self):
        self.bst.GenerateTree([])
        self.assertIsNone(self.bst.Root)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_single_element(self):
        self.bst.GenerateTree([10])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 10)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))
        self.assertTrue(self.bst.IsBST(self.bst.Root))

    def test_two_elements(self):
        self.bst.GenerateTree([10, 20])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 10)
        self.assertIsNotNone(self.bst.Root.RightChild)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 20)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))
        self.assertTrue(self.bst.IsBST(self.bst.Root))

    def test_three_elements(self):
        self.bst.GenerateTree([10, 20, 30])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 20)
        self.assertIsNotNone(self.bst.Root.LeftChild)
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 10)
        self.assertIsNotNone(self.bst.Root.RightChild)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 30)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))
        self.assertTrue(self.bst.IsBST(self.bst.Root))

    def test_larger_array(self):
        array = [3, 1, 5, 2, 4]
        self.bst.GenerateTree(array)

        # Проверка структуры дерева
        root = self.bst.Root
        self.assertIsNotNone(root)
        self.assertEqual(root.NodeKey, 3)

        left = root.LeftChild
        self.assertIsNotNone(left)
        self.assertEqual(left.NodeKey, 2)

        left_left = left.LeftChild
        self.assertIsNotNone(left_left)
        self.assertEqual(left_left.NodeKey, 1)

        right = root.RightChild
        self.assertIsNotNone(right)
        self.assertEqual(right.NodeKey, 5)

        right_left = right.LeftChild
        self.assertIsNotNone(right_left)
        self.assertEqual(right_left.NodeKey, 4)

        # Проверка сбалансированности
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

        # Проверка корректности BST
        self.assertTrue(self.bst.IsBST(self.bst.Root))


if __name__ == '__main__':
    unittest.main()
