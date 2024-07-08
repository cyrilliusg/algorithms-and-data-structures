import unittest

from sorting.insertion_sorting.knuth_sequence import KnuthSequence


class TestKnuthSequence(unittest.TestCase):
    def test_zero_size(self):
        self.assertEqual(KnuthSequence(0), [], "Ошибка: для size 0 ожидается []")

    def test_minimal_positive_size(self):
        self.assertEqual(KnuthSequence(1), [], "Ошибка: для size 1 ожидается []")
        self.assertEqual(KnuthSequence(4), [1], "Ошибка: для size 4 ожидается [1]")

    def test_small_sizes(self):
        self.assertEqual(KnuthSequence(5), [4, 1], "Ошибка: для size 5 ожидается [4, 1]")
        self.assertEqual(KnuthSequence(15), [13, 4, 1], "Ошибка: для size 15 ожидается [13, 4, 1]")

    def test_large_sizes(self):
        self.assertEqual(KnuthSequence(121), [40, 13, 4, 1], "Ошибка: для size 121 ожидается [40, 13, 4, 1]")
        self.assertEqual(KnuthSequence(122), [121, 40, 13, 4, 1], "Ошибка: для size 122 ожидается [121, 40, 13, 4, 1]")

    def test_very_large_size(self):
        self.assertEqual(KnuthSequence(1000), [364, 121, 40, 13, 4, 1],
                         "Ошибка: для size 1000 ожидается [364, 121, 40, 13, 4, 1]")


if __name__ == '__main__':
    unittest.main()
