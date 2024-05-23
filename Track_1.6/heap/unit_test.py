import random
import unittest
from .heap import Heap


class TestHeap(unittest.TestCase):

    def test_make_heap(self):
        heap = Heap()
        heap.MakeHeap([3, 2, 1, 5, 4], 2)
        self.assertEqual(heap.HeapArray[:heap.size], [5, 4, 1, 2, 3])

    def test_get_max(self):
        heap = Heap()
        heap.MakeHeap([3, 2, 1, 5, 4], 2)
        max_elem = heap.GetMax()
        self.assertEqual(max_elem, 5)
        self.assertEqual(heap.HeapArray[:heap.size], [4, 3, 1, 2])

    def test_add(self):
        heap = Heap()
        heap.MakeHeap([3, 2, 1, 5, 4], 2)
        result = heap.Add(6)
        self.assertTrue(result)
        self.assertEqual(heap.HeapArray[:heap.size], [6, 4, 5, 2, 3, 1])

    def test_add_to_full_heap(self):
        heap = Heap()
        heap.MakeHeap([3, 2, 1, 5, 4], 2)
        heap.Add(6)
        heap.Add(7)
        result = heap.Add(8)
        self.assertFalse(result)
        self.assertEqual(heap.HeapArray[:heap.size], [7, 4, 6, 2, 3, 1, 5])

    def test_get_max_from_empty_heap(self):
        heap = Heap()
        max_elem = heap.GetMax()
        self.assertEqual(max_elem, -1)

    def test_large_heap(self):
        depth = 10  # Глубина кучи
        num_elements = 2 ** (depth + 1) - 1
        elements = list(range(num_elements))
        random.shuffle(elements)

        heap = Heap()
        heap.MakeHeap(elements, depth)

        sorted_elements = sorted(elements, reverse=True)
        for expected_max in sorted_elements:
            self.assertEqual(heap.GetMax(), expected_max)

    def test_large_heap_add(self):
        depth = 10
        num_elements = 2 ** (depth + 1) - 1
        elements = list(range(num_elements - 1))

        heap = Heap()
        heap.MakeHeap(elements, depth)

        self.assertTrue(heap.Add(num_elements))
        self.assertFalse(heap.Add(num_elements + 1))


if __name__ == '__main__':
    unittest.main()
