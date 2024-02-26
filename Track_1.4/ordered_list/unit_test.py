import unittest
import random
from ordered_list import OrderedList


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


class OrderedListTests(unittest.TestCase):
    """
    Тесты для методов упорядоченного связного списка.
    Этот набор охватывает вставку, удаление и упорядочивание как по возрастанию, так и по убыванию.
    """

    def verify_list_order(self, expected_values, ordered_list, ascending=True):
        """
        Проверяет порядок списка на соответствие ожидаемым значениям.
        Выводит значения перед сортировкой для отладки и утверждает, что список соответствует ожидаемому порядку.
        """
        self.assertEqual(len(expected_values), ordered_list.len(), "List length mismatch.")

        expected_values.sort(reverse=not ascending)

        current_node = ordered_list.head
        for expected_value in expected_values:
            self.assertEqual(expected_value, current_node.value, "Value mismatch in the list.")
            current_node = current_node.next

    def test_delete_single_occurrence_from_populated_list(self):
        """
        Проверяет удаление одного значения из списка с несколькими значениями.
        """
        values = [1, 2, 3, 4, 5]
        ordered_list = OrderedList(True)

        for value in values:
            ordered_list.add(value)

        self.verify_list_order(values, ordered_list)

        # Deleting a single occurrence
        ordered_list.delete(2)
        values.remove(2)

        self.verify_list_order(values, ordered_list)

        self.assertEqual(4, ordered_list.len())
        self.assertEqual(1, ordered_list.head.value)
        self.assertEqual(5, ordered_list.tail.value)

    def test_delete_all_occurrences_from_populated_list(self):
        """
        Проверяет удаление всех вхождений значения в списке, заполненном одинаковыми значениями.
        """
        values = [2] * 10
        ordered_list = OrderedList(True)

        for value in values:
            ordered_list.add(value)

        self.verify_list_order(values, ordered_list)

        # Deleting all occurrences of a value
        ordered_list.delete(2)

        self.assertEqual(0, ordered_list.len())
        self.assertIsNone(ordered_list.head)
        self.assertIsNone(ordered_list.tail)

    def test_delete_from_empty_list(self):
        """
        Проверяет удаление из пустого списка.
        """
        ordered_list = OrderedList(True)

        # Attempting to delete from an empty list
        ordered_list.delete(2)

        self.assertEqual(0, ordered_list.len())
        self.assertIsNone(ordered_list.head)
        self.assertIsNone(ordered_list.tail)

    @repeat_test(times=3)
    def test_delete_single_value_from_single_item_list(self):
        """
        Тесты удаления одного значения из списка, содержащего только одно значение, повторяются три раза.
        """
        for _ in range(3):
            value = random.randint(-1000, 1000)
            ordered_list = OrderedList(True)

            ordered_list.add(value)
            self.verify_list_order([value], ordered_list)

            ordered_list.delete(value)

            self.assertEqual(0, ordered_list.len())
            self.assertIsNone(ordered_list.head)
            self.assertIsNone(ordered_list.tail)

    def test_desc_delete_one_value_many_vals(self):
        test_arr = [1, 2, 3, 4, 5]
        asc = False
        l_list = OrderedList(asc)

        for item in test_arr:
            l_list.add(item)

        # тест вставки
        self.verify_list_order(test_arr, l_list, asc)

        # Удаление 1 вхождения
        l_list.delete(2)
        test_arr.remove(2)

        self.verify_list_order(test_arr, l_list, asc)

        self.assertEqual(4, l_list.len())
        self.assertEqual(l_list.tail.value, 1)
        self.assertEqual(l_list.head.value, 5)

    def test_desc_delete_all_value_many_vals(self):
        test_arr = [2] * 10
        asc = False
        l_list = OrderedList(asc)

        for item in test_arr:
            l_list.add(item)

        # тест вставки
        self.verify_list_order(test_arr, l_list, asc)

        # Удаление 1 вхождения
        l_list.delete(2)

        self.assertEqual(0, l_list.len())
        self.assertEqual(None, l_list.head)
        self.assertEqual(None, l_list.tail)

    @repeat_test(times=3)
    def test_desc_delete_one_value_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        value = random.choice(test_arr)
        l_list = OrderedList(False)

        # Создание связанного списка
        for item in test_arr:
            l_list.add(item)

        # тест вставки
        self.verify_list_order(test_arr, l_list, False)

        # Удаление первого вхождения
        l_list.delete(value)
        test_arr.remove(value)  # Удаляем первое вхождение

        self.assertEqual(0, l_list.len())
        self.assertEqual(None, l_list.head)
        self.assertEqual(None, l_list.tail)

    @repeat_test(times=3)
    def test_desc_delete_all_occurrences_many_values(self):
        test_arr = random.sample(range(10, 20), 9)
        value = random.choice(test_arr)
        l_list = OrderedList(False)

        # Создание связанного списка
        for item in test_arr:
            l_list.add(item)
        # тест вставки
        self.verify_list_order(test_arr, l_list, False)

        # Удаление всех вхождений
        l_list.delete(value)
        # Создание ожидаемой последовательности
        expected_sequence = [item for item in test_arr if item != value]

        # Проверка последовательности
        self.verify_list_order(expected_sequence, l_list, False)

        self.assertEqual(len(expected_sequence), l_list.len())
        self.assertEqual(expected_sequence[0], l_list.head.value)
        self.assertEqual(expected_sequence[-1], l_list.tail.value)


if __name__ == '__main__':
    unittest.main()
