import unittest
from sorting import bubble_sort
import random
import pytest


@pytest.mark.repeat(3)
def test_random_sample():
    test_arr = random.sample(range(-1000, 1000), 20)
    target_arr = test_arr.copy()
    bubble_sort(test_arr)
    assert test_arr == sorted(target_arr)


def repeat_test(times):
    """
    кастомный декоратор для повтора вызова функции times раз
    """

    def repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return repeat


class UnitTestSortMethods(unittest.TestCase):
    """
    Тест пузырьковой сортировки

    Рассмотрим следующие состояния:
    1. числа в случайном порядке
    2. уже отсортированный список в обратном порядке
    3. список в котором одинаковые значения
    4. Уже отсортированный список
    5. пустой список
    """

    @pytest.mark.repeat(3)
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

    def test_empty_list(self):
        test_arr = []
        self.comparing(test_arr)

    def comparing(self, test_arr):
        target_arr = test_arr.copy()
        self.assertEqual(bubble_sort(test_arr), target_arr.sort())


if __name__ == '__main__':
    # тестируем библиотекой pytest
    test_random_sample()
    # тестируем библиотекой unittest
    unittest.main()
