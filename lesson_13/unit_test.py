import unittest
from sorting import bubble_sort
import random


class TestStringMethods(unittest.TestCase):
    """
    Тест пузырьковой сортировки

    Рассмотрим следующие состояния:
    1. числа в случайном порядке
    2. уже отсортированный список в обратном порядке
    3. список в котором одинаковые значения
    4. Уже отсортированный список
    """

    def test_random_sample(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        self.comparing(test_arr)

    def test_reverse_sorted_sample(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        test_arr.sort()
        test_arr.reverse()
        self.comparing(test_arr)

    def test_same_values(self):
        test_arr = [0] * 10
        self.comparing(test_arr)

    def test_sorted_sample(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        test_arr.sort()
        self.comparing(test_arr)

    def comparing(self, test_arr):
        target_arr = test_arr.copy()
        self.assertEqual(bubble_sort(test_arr), target_arr.sort())


if __name__ == '__main__':
    unittest.main()
