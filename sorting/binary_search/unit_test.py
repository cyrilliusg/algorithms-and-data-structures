import unittest

from sorting.binary_search.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def run_search(self, bs, N):
        while bs.GetResult() == 0:
            bs.Step(N)

    def test_empty_array(self):
        bs = BinarySearch([])
        self.run_search(bs, 5)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_single_element_found(self):
        bs = BinarySearch([10])
        self.run_search(bs, 10)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_single_element_not_found(self):
        bs = BinarySearch([10])
        self.run_search(bs, 5)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_all_elements_same_found(self):
        bs = BinarySearch([7, 7, 7, 7, 7])
        self.run_search(bs, 7)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_all_elements_same_not_found(self):
        bs = BinarySearch([7, 7, 7, 7, 7])
        self.run_search(bs, 5)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_element_in_middle(self):
        bs = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.run_search(bs, 5)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_element_near_start(self):
        bs = BinarySearch([10, 20, 30, 40, 50])
        self.run_search(bs, 20)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_element_near_end(self):
        bs = BinarySearch([10, 20, 30, 40, 50])
        self.run_search(bs, 40)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_large_array_element_not_found(self):
        large_array = list(range(0, 1000000, 2))
        bs = BinarySearch(large_array)
        self.run_search(bs, 999999)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_large_array_element_found(self):
        large_array = list(range(0, 1000000, 2))
        bs = BinarySearch(large_array)
        self.run_search(bs, 500000)
        self.assertEqual(bs.GetResult(), 1)  # Ожидаемое: элемент найден

    def test_search_after_exceeding_bounds(self):
        bs = BinarySearch([1, 3, 5, 7, 9])
        self.run_search(bs, 2)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден
        self.run_search(bs, 10)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_element_not_in_bounds(self):
        bs = BinarySearch([10, 20, 30, 40, 50])
        self.run_search(bs, 5)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден

    def test_element_greater_than_all(self):
        bs = BinarySearch([10, 20, 30, 40, 50])
        self.run_search(bs, 60)
        self.assertEqual(bs.GetResult(), -1)  # Ожидаемое: элемент не найден


if __name__ == '__main__':
    unittest.main()
