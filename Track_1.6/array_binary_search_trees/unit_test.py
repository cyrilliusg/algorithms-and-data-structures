import unittest

from .array_binary_search_trees import aBST


class TestABST(unittest.TestCase):
    def setUp(self):
        self.tree_depth = 3
        self.tree = aBST(self.tree_depth)
        self.values = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]

    def test_add_key(self):
        for value in self.values:
            with self.subTest(value=value):
                self.tree.AddKey(value)

    def test_find_existing_key(self):
        for value in self.values:
            self.tree.AddKey(value)
        for value in self.values:
            with self.subTest(value=value):
                index = self.tree.FindKeyIndex(value)
                self.assertTrue(index >= 0, f"Ключ {value} не найден, но должен быть.")

    def test_find_missing_key(self):
        for value in self.values:
            self.tree.AddKey(value)
        missing_value = self.tree.tree_size + 1
        index = self.tree.FindKeyIndex(missing_value)
        self.assertTrue(index < 0, f"Ключ {missing_value} есть, но его не должно быть.")

    def test_tree_structure(self):
        for value in self.values:
            self.tree.AddKey(value)
        self.assertEqual(len(self.tree.Tree), 15, "Структура дерева некорректна.")


if __name__ == "__main__":
    unittest.main()
