import unittest

from sorting.galloping_binary_search.binary_search import BinarySearch, GallopingSearch


class TestGallopingSearch(unittest.TestCase):

    def test_element_at_start(self):
        # Элемент находится в начале массива
        self.assertTrue(GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

    def test_element_at_end(self):
        # Элемент находится в конце массива
        self.assertTrue(GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_element_in_middle(self):
        # Элемент находится в середине массива
        self.assertTrue(GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

    def test_element_not_found(self):
        # Элемент отсутствует в массиве
        self.assertFalse(GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    def test_single_element_array_found(self):
        # Массив из одного элемента, элемент найден
        self.assertTrue(GallopingSearch([5], 5))

    def test_single_element_array_not_found(self):
        # Массив из одного элемента, элемент не найден
        self.assertFalse(GallopingSearch([5], 10))

    def test_two_elements_array(self):
        # Массив из двух элементов
        self.assertTrue(GallopingSearch([3, 8], 8))
        self.assertFalse(GallopingSearch([3, 8], 5))

    def test_repeated_elements(self):
        # Массив с повторяющимися элементами
        self.assertTrue(GallopingSearch([1, 1, 1, 1, 2, 3, 3, 3, 4, 5], 3))
        self.assertFalse(GallopingSearch([1, 1, 1, 1, 2, 3, 3, 3, 4, 5], 6))

    def test_empty_array(self):
        # Пустой массив
        self.assertFalse(GallopingSearch([], 1))


if __name__ == '__main__':
    unittest.main()