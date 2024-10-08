import unittest

from sorting.merge_sort.merge_sort import MergeSort


class TestMergeSort(unittest.TestCase):

    def test_example_case(self):
        arr = [7, 5, 6, 4, 3, 1, 2]
        expected = [1, 2, 3, 4, 5, 6, 7]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_array(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        arr = []
        expected = []
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_single_element_array(self):
        arr = [1]
        expected = [1]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_two_element_array(self):
        arr = [2, 1]
        expected = [1, 2]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_three_element_array(self):
        arr = [3, 1, 2]
        expected = [1, 2, 3]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_mixed_array(self):
        arr = [1, 3, 4, 6, 5, 2, 8]
        expected = [1, 2, 3, 4, 5, 6, 8]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)

    def test_small_mixed_array(self):
        arr = [6, 5, 7]
        expected = [5, 6, 7]
        arr = MergeSort(arr)
        self.assertEqual(arr, expected)


if __name__ == '__main__':
    unittest.main()
