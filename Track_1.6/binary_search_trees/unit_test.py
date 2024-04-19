import unittest

# Предположим, что классы BST, BSTNode и т.д. определены в модуле bst_module
from .binary_search_trees import BST, BSTNode


class TestBST(unittest.TestCase):
    def setUp(self):
        # Инициализация дерева с корневым узлом
        self.bst = BST(BSTNode(50, 'Root', None))
        self.bst.AddKeyValue(30, 'Left Child')
        self.bst.AddKeyValue(70, 'Right Child')

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


if __name__ == '__main__':
    unittest.main()
