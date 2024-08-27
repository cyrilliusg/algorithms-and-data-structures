import unittest

from sorting.galloping_binary_search.binary_search import BinarySearch


class TestGallopingSearch(unittest.TestCase):

    def test_element_at_start(self):
        # Элемент находится в начале массива
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

    def test_element_at_end(self):
        # Элемент находится в конце массива
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_element_in_middle(self):
        # Элемент находится в середине массива
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

    def test_element_not_found(self):
        # Элемент отсутствует в массиве
        search = BinarySearch([])
        self.assertFalse(search.GallopingSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    def test_single_element_array_found(self):
        # Массив из одного элемента, элемент найден
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([5], 5))

    def test_single_element_array_not_found(self):
        # Массив из одного элемента, элемент не найден
        search = BinarySearch([])
        self.assertFalse(search.GallopingSearch([5], 10))

    def test_two_elements_array(self):
        # Массив из двух элементов
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([3, 8], 8))
        self.assertFalse(search.GallopingSearch([3, 8], 5))

    def test_repeated_elements(self):
        # Массив с повторяющимися элементами
        search = BinarySearch([])
        self.assertTrue(search.GallopingSearch([1, 1, 1, 1, 2, 3, 3, 3, 4, 5], 3))
        self.assertFalse(search.GallopingSearch([1, 1, 1, 1, 2, 3, 3, 3, 4, 5], 6))

    def test_empty_array(self):
        # Пустой массив
        search = BinarySearch([])
        self.assertFalse(search.GallopingSearch([], 1))


if __name__ == '__main__':
    unittest.main()