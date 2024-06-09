import unittest
import random
from bidirectional_linked_list import Node
from bdl_with_one_dummy import Dummy


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
        l_list = Dummy()

        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление 1 вхождения
        l_list.delete(2, all=False)
        test_arr.remove(2)

        self.assertEqual(l_list.len(), len(test_arr))
        self.assertEqual(l_list.dummy.next.value, 2)
        self.assertEqual(l_list.dummy.prev.value, 2)

    def test_delete_all_value_many_vals(self):
        test_arr = [2] * 10
        l_list = Dummy()

        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление всех вхождений
        l_list.delete(2, all=True)

        test_arr = []
        self.assertEqual(l_list.len(), len(test_arr))
        self.assertEqual(l_list.dummy.next, l_list.dummy)
        self.assertEqual(l_list.dummy.prev, l_list.dummy)

    def test_delete_one_value_empty_list(self):
        l_list = Dummy()

        # Попытка удаления 1 вхождения
        l_list.delete(2, all=False)

        self.assertEqual(l_list.len(), 0)
        self.assertEqual(l_list.dummy.next, l_list.dummy)
        self.assertEqual(l_list.dummy.prev, l_list.dummy)

    @repeat_test(times=3)
    def test_delete_one_value_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        value = random.choice(test_arr)
        l_list = Dummy()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление первого вхождения
        l_list.delete(value)
        test_arr.remove(value)  # Удаляем первое вхождение

        self.assertEqual(l_list.len(), len(test_arr))
        self.assertEqual(l_list.dummy.next, l_list.dummy)
        self.assertEqual(l_list.dummy.prev, l_list.dummy)

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        test_arr = random.sample(range(10, 20), 20)
        value = random.choice(test_arr)
        l_list = Dummy()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление всех вхождений
        l_list.delete(value, all=True)

        # Создание ожидаемой последовательности
        expected_sequence = [item for item in test_arr if item != value]

        # Проверка последовательности
        node = l_list.dummy.next
        for expected_value in expected_sequence:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertEqual(l_list.len(), len(expected_sequence))
        self.assertEqual(l_list.dummy.next.value, expected_sequence[0])
        self.assertEqual(l_list.dummy.prev.value, expected_sequence[-1])

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        expected_sequence = random.sample(range(-1000, 1000), 20)
        value = random.choice(expected_sequence)
        l_list = Dummy()

        # Создание связанного списка
        for item in expected_sequence:
            l_list.add_in_tail(Node(item))

        # Удаление 1 вхождения
        l_list.delete(value, all=False)
        # Создание ожидаемой последовательности
        expected_sequence.remove(value)

        # Проверка последовательности
        node = l_list.dummy.next
        for expected_value in expected_sequence:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertEqual(l_list.len(), len(expected_sequence))
        self.assertEqual(l_list.dummy.next.value, expected_sequence[0])
        self.assertEqual(l_list.dummy.prev.value, expected_sequence[-1])

    def test_insert_in_empty_list(self):
        l_list = Dummy()
        value = 1

        l_list.insert(None, Node(value))

        self.assertEqual(l_list.len(), 1)
        self.assertEqual(l_list.dummy.next.value, 1)
        self.assertEqual(l_list.dummy.prev.value, 1)

    def test_insert_in_one_val_list(self):
        l_list = Dummy()
        node = Node(1)
        value = 2
        l_list.add_in_tail(node)
        l_list.insert(node, Node(value))

        node = l_list.dummy.next
        for val in [1, 2]:
            self.assertEqual(val, node.value)
            node = node.next

        self.assertEqual(l_list.len(), 2)
        self.assertEqual(l_list.dummy.next.value, 1)
        self.assertEqual(l_list.dummy.prev.value, 2)

    def test_insert_in_one_val_without_afternode(self):
        l_list = Dummy()
        node = Node(1)
        value = 2
        l_list.add_in_tail(node)
        l_list.insert(None, Node(value))

        node = l_list.dummy.next
        for val in [1, 2]:
            self.assertEqual(val, node.value)
            node = node.next

        self.assertEqual(l_list.len(), 2)
        self.assertEqual(l_list.dummy.next.value, 1)
        self.assertEqual(l_list.dummy.prev.value, 2)

    def test_insert_in_many_val_list(self):
        l_list = Dummy()
        l_list.add_in_tail(Node(1))
        l_list.add_in_tail(Node(3))

        value = 2
        l_list.insert(l_list.dummy.next, Node(value))  # в середину

        node = l_list.dummy.next
        for val in [1, 2, 3]:
            self.assertEqual(val, node.value)
            node = node.next

        self.assertEqual(l_list.len(), 3)
        self.assertEqual(l_list.dummy.next.value, 1)
        self.assertEqual(l_list.dummy.prev.value, 3)

    def test_insert_in_many_val_without_afternode(self):
        l_list = Dummy()
        l_list.add_in_tail(Node(1))
        l_list.add_in_tail(Node(3))

        value = 2
        l_list.insert(None, Node(value))  # в конец

        node = l_list.dummy.next
        for val in [1, 3, 2]:
            self.assertEqual(val, node.value)
            node = node.next

        self.assertEqual(l_list.len(), 3)
        self.assertEqual(l_list.dummy.next.value, 1)
        self.assertEqual(l_list.dummy.prev.value, 2)


if __name__ == '__main__':
    unittest.main()
