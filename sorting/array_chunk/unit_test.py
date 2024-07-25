import unittest

from sorting.array_chunk.array_chunk import ArrayChunk


class TestArrayChunk(unittest.TestCase):

    def test_example_case(self):
        arr = [7, 5, 6, 4, 3, 1, 2]
        expected = [2, 1, 3, 4, 6, 5, 7]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 3)
        self.assertEqual(arr, expected)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 3)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_array(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 3)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        arr = []
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 0)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 0)
        self.assertEqual(arr, [1])

    def test_two_element_array(self):
        arr = [2, 1]
        expected = [1, 2]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 1)
        self.assertEqual(arr, expected)

    def test_three_element_array(self):
        arr = [3, 1, 2]
        expected = [1, 2, 3]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 1)
        self.assertEqual(arr, expected)

    def test_mixed_array(self):
        arr = [1, 3, 4, 6, 5, 2, 8]
        expected = [1, 2, 3,  4, 5, 6, 8]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 3)
        self.assertEqual(arr, expected)

    def test_small_mixed_array(self):
        arr = [6, 5, 7]
        expected = [5, 6, 7]
        pivot_index = ArrayChunk(arr)
        self.assertEqual(pivot_index, 1)
        self.assertEqual(arr, expected)


if __name__ == '__main__':
    unittest.main()
