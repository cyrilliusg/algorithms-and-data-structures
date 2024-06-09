import unittest
import random
from bidirectional_linked_list import Node, LinkedList2


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
    Тест методов связанного списка

    Рассмотрим следующие состояния:
    1. Один элемент
    2. Много элементов в списке
    3. Пустой список

    И по качеству содержимого:
    1. Одинаковые значения
    2. Случайные значения
    """

    def test_delete_one_value_many_vals(self):
        test_arr = [2] * 10
        l_list = LinkedList2()

        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление 1 вхождения
        l_list.delete(2, all=False)

        self.assertEqual(l_list.len(), 9)
        self.assertEqual(l_list.head.value, 2)
        self.assertEqual(l_list.tail.value, 2)

    def test_delete_all_value_many_vals(self):
        test_arr = [2] * 10
        l_list = LinkedList2()

        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление всех вхождений
        l_list.delete(2, all=True)

        self.assertEqual(l_list.len(), 0)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_delete_one_value_empty_list(self):
        l_list = LinkedList2()

        # Попытка удаления 1 вхождения
        l_list.delete(2, all=False)

        self.assertEqual(l_list.len(), 0)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    @repeat_test(times=3)
    def test_delete_one_value_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        value = random.choice(test_arr)
        l_list = LinkedList2()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление первого вхождения
        l_list.delete(value)
        test_arr.remove(value)  # Удаляем первое вхождение

        self.assertEqual(l_list.len(), 0)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        test_arr = random.sample(range(10, 20), 20)
        value = random.choice(test_arr)
        l_list = LinkedList2()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление всех вхождений
        l_list.delete(value, all=True)

        # Создание ожидаемой последовательности
        expected_sequence = [item for item in test_arr if item != value]

        # Проверка последовательности
        node = l_list.head
        for expected_value in expected_sequence:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertIsNone(node)  # Убедимся, что больше нет элементов в списке
        self.assertEqual(l_list.len(), len(expected_sequence))
        self.assertEqual(l_list.head.value, expected_sequence[0])
        self.assertEqual(l_list.tail.value, expected_sequence[-1])

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        expected_sequence = random.sample(range(-1000, 1000), 20)
        value = random.choice(expected_sequence)
        l_list = LinkedList2()

        # Создание связанного списка
        for item in expected_sequence:
            l_list.add_in_tail(Node(item))

        # Удаление 1 вхождения
        l_list.delete(value, all=False)
        # Создание ожидаемой последовательности
        expected_sequence.remove(value)

        # Проверка последовательности
        node = l_list.head
        for expected_value in expected_sequence:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertIsNone(node)  # Убедимся, что больше нет элементов в списке
        self.assertEqual(l_list.len(), len(expected_sequence))
        self.assertEqual(l_list.head.value, expected_sequence[0])
        self.assertEqual(l_list.tail.value, expected_sequence[-1])


if __name__ == '__main__':
    # тестируем библиотекой unittest
    unittest.main()
