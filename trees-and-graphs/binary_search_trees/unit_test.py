import unittest

from .binary_search_trees import BST, BSTNode


class TestBST(unittest.TestCase):
    def setUp(self):
        # Инициализация дерева с корневым узлом
        self.bst = BST(BSTNode(50, 'Root', None))
        self.bst.AddKeyValue(30, 'Left Child')
        self.bst.AddKeyValue(70, 'Right Child')

        # Empty Tree - BST initialized with a node but no children
        empty_root = BSTNode(None, None, None)  # Simulating an empty tree with a dummy root node
        self.empty_tree = BST(empty_root)

        # Single Node Tree
        single_node = BSTNode(10, "Root", None)
        self.single_node_tree = BST(single_node)

        # Multi-node Tree
        root = BSTNode(10, "Root", None)
        left = BSTNode(5, "Left", root)
        right = BSTNode(15, "Right", root)
        root.LeftChild = left
        root.RightChild = right
        self.multi_node_tree = BST(root)

    def test_find_node_by_key(self):
        # Поиск отсутствующего ключа (должен вернуть ложь и указать, куда добавить новый узел)
        find = self.bst.FindNodeByKey(10)
        self.assertFalse(find.NodeHasKey)
        self.assertTrue(find.ToLeft)
        self.assertEqual(find.Node.NodeKey, 30)

        find = self.bst.FindNodeByKey(90)
        self.assertFalse(find.NodeHasKey)
        self.assertFalse(find.ToLeft)
        self.assertEqual(find.Node.NodeKey, 70)

        # Поиск существующего ключа
        find = self.bst.FindNodeByKey(70)
        self.assertTrue(find.NodeHasKey)
        self.assertEqual(find.Node.NodeValue, 'Right Child')

    def test_add_key_value(self):
        # Добавление нового узла, проверка его наличия
        self.assertFalse(self.bst.FindNodeByKey(20).NodeHasKey)
        self.assertTrue(self.bst.AddKeyValue(20, 'New Left Child'))
        self.assertTrue(self.bst.FindNodeByKey(20).NodeHasKey)

        # Попытка добавить существующий ключ
        self.assertFalse(self.bst.AddKeyValue(70, 'Duplicate Key'))

    def test_find_min_max(self):
        # Поиск максимального и минимального ключей
        self.assertEqual(self.bst.FinMinMax(FromNode=self.bst.Root, FindMax=True).NodeKey, 70)
        self.assertEqual(self.bst.FinMinMax(FromNode=self.bst.Root, FindMax=False).NodeKey, 30)

        # Проверка поддеревьев
        self.assertEqual(self.bst.FinMinMax(FromNode=self.bst.Root.LeftChild, FindMax=True).NodeKey, 30)
        self.assertEqual(self.bst.FinMinMax(FromNode=self.bst.Root.RightChild, FindMax=False).NodeKey, 70)

    def test_delete_node_by_key(self):
        # Удаление узла по ключу
        self.assertTrue(self.bst.FindNodeByKey(30).NodeHasKey)
        self.assertTrue(self.bst.DeleteNodeByKey(30))
        self.assertFalse(self.bst.FindNodeByKey(30).NodeHasKey)
        self.assertFalse(self.bst.DeleteNodeByKey(30))  # Удаление уже удаленного узла

    def test_count(self):
        # Подсчет узлов в дереве
        self.assertEqual(self.bst.Count(), 3)
        self.bst.AddKeyValue(90, 'New Right Child')
        self.assertEqual(self.bst.Count(), 4)

    def test_empty_tree_deep_all_nodes(self):
        self.assertEqual(self.empty_tree.DeepAllNodes(0), (self.empty_tree.Root,))
        self.assertEqual(self.empty_tree.DeepAllNodes(1), (self.empty_tree.Root,))
        self.assertEqual(self.empty_tree.DeepAllNodes(2), (self.empty_tree.Root,))

    def test_single_node_tree_deep_all_nodes(self):
        expected_node_tuple = (self.single_node_tree.Root,)
        self.assertEqual(self.single_node_tree.DeepAllNodes(0), expected_node_tuple)
        self.assertEqual(self.single_node_tree.DeepAllNodes(1), expected_node_tuple)
        self.assertEqual(self.single_node_tree.DeepAllNodes(2), expected_node_tuple)

    def test_multi_node_tree_traversals(self):
        in_order = (
        self.multi_node_tree.Root.LeftChild, self.multi_node_tree.Root, self.multi_node_tree.Root.RightChild)
        post_order = (
        self.multi_node_tree.Root.LeftChild, self.multi_node_tree.Root.RightChild, self.multi_node_tree.Root)
        pre_order = (
        self.multi_node_tree.Root, self.multi_node_tree.Root.LeftChild, self.multi_node_tree.Root.RightChild)
        self.assertEqual(self.multi_node_tree.DeepAllNodes(0), in_order)
        self.assertEqual(self.multi_node_tree.DeepAllNodes(1), post_order)
        self.assertEqual(self.multi_node_tree.DeepAllNodes(2), pre_order)

    def test_invert_tree(self):
        self.multi_node_tree.InvertTree()
        # Ensure root's children have been swapped
        self.assertEqual(self.multi_node_tree.Root.LeftChild.NodeKey, 15)
        self.assertEqual(self.multi_node_tree.Root.RightChild.NodeKey, 5)


if __name__ == '__main__':
    unittest.main()
