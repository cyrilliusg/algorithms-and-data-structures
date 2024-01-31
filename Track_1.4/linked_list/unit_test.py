import unittest
import random
from linked_list import Node, LinkedList


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
    1. Один элемент
    2. Много элементов в списке
    3. Пустой список
    """

    @repeat_test(times=3)
    def test_delete_one_value_many_vals(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        value = random.choice(test_arr)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление первого вхождения
        l_list.delete(value)
        test_arr.remove(value)  # Удаляем первое вхождение

        # Проверка последовательности
        node = l_list.head
        for expected_value in test_arr:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertIsNone(node)  # Убедимся, что больше нет элементов в списке

    @repeat_test(times=3)
    def test_delete_one_value_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        value = random.choice(test_arr)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Удаление первого вхождения
        l_list.delete(value)
        test_arr.remove(value)  # Удаляем первое вхождение

        # Проверка последовательности
        node = l_list.head
        for expected_value in test_arr:
            self.assertEqual(node.value, expected_value)
            node = node.next

        self.assertIsNone(node)  # Убедимся, что больше нет элементов в списке

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        test_arr = random.sample(range(10, 20), 20)
        value = random.choice(test_arr)
        l_list = LinkedList()

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

    @repeat_test(times=3)
    def test_delete_all_occurrences_many_values(self):
        test_arr = random.sample(range(10, 20), 1)
        value = random.choice(test_arr)
        l_list = LinkedList()

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

    @repeat_test(times=3)
    def test_insert_node_at_start_many_vals(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Создание и вставка нового узла
        new_value = 1234
        new_node = Node(new_value)
        l_list.insert(None, new_node)

        # Проверка, что новый узел первый в списке
        self.assertEqual(l_list.head.value, new_value)

        # Проверка остальной последовательности
        node = l_list.head.next
        for expected_value in test_arr:
            self.assertEqual(node.value, expected_value)
            node = node.next

    @repeat_test(times=3)
    def test_insert_node_at_start_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Создание и вставка нового узла
        new_value = 1234
        new_node = Node(new_value)
        l_list.insert(None, new_node)

        # Проверка, что новый узел первый в списке
        self.assertEqual(l_list.head.value, new_value)

        # Проверка остальной последовательности
        node = l_list.head.next
        for expected_value in test_arr:
            self.assertEqual(node.value, expected_value)
            node = node.next

    @repeat_test(times=3)
    def test_insert_node_after_another(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Выбор случайного узла для вставки после него
        after_node_index = random.randint(0, len(test_arr) - 1)
        after_node = l_list.find(test_arr[after_node_index])

        # Создание и вставка нового узла
        new_value = 1234
        l_list.insert(after_node, Node(new_value))

        # Проверка расположения нового узла
        node = l_list.head
        for i in range(after_node_index + 1):  # Проходим до узла после которого вставляли
            self.assertEqual(node.value, test_arr[i])
            node = node.next

        # Проверка нового узла
        self.assertEqual(node.value, new_value)

        # Проверка остальной части списка
        node = node.next
        for expected_value in test_arr[after_node_index + 1:]:
            self.assertEqual(node.value, expected_value)
            node = node.next

    @repeat_test(times=3)
    def test_insert_node_after_another_one_val(self):
        test_arr = random.sample(range(-1000, 1000), 1)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Выбор случайного узла для вставки после него
        after_node_index = random.randint(0, len(test_arr) - 1)
        after_node = l_list.find(test_arr[after_node_index])

        # Создание и вставка нового узла
        new_value = 1234
        l_list.insert(after_node, Node(new_value))

        # Проверка расположения нового узла
        node = l_list.head
        for i in range(after_node_index + 1):  # Проходим до узла после которого вставляли
            self.assertEqual(node.value, test_arr[i])
            node = node.next

        # Проверка нового узла
        self.assertEqual(node.value, new_value)

        # Проверка остальной части списка
        node = node.next
        for expected_value in test_arr[after_node_index + 1:]:
            self.assertEqual(node.value, expected_value)
            node = node.next

    def test_find_in_list(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Выбор случайного значения для поиска
        value_to_find = random.choice(test_arr)
        found_node = l_list.find(value_to_find)

        # Проверка наличия значения в списке
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.value, value_to_find)

    def test_find_not_in_list(self):
        test_arr = random.sample(range(-1000, 1000), 20)
        l_list = LinkedList()

        # Создание связанного списка
        for item in test_arr:
            l_list.add_in_tail(Node(item))

        # Выбор значения, которого нет в списке
        value_not_in_list = 2000  # Выбрано значение, которого точно нет в списке
        found_node = l_list.find(value_not_in_list)

        # Проверка отсутствия значения в списке
        self.assertIsNone(found_node)

    def test_find_in_empty_list(self):
        l_list = LinkedList()

        # Поиск в пустом списке
        found_node = l_list.find(123)

        # Проверка результата
        self.assertIsNone(found_node)


if __name__ == '__main__':
    # тестируем библиотекой unittest
    unittest.main()
