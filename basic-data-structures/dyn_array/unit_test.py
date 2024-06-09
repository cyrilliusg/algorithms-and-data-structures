import unittest
from dyn_array import DynArray


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


class UnitTestDynArray(unittest.TestCase):
    """
    Тест методов динамического массива

    Рассмотрим следующие случаи:
    -- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
    -- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);
    -- попытка вставки элемента в недопустимую позицию;
    -- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
    -- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
    -- попытка удаления элемента в недопустимой позиции.
    """

    def test_delete_one_value(self):
        """
        Удаление значения из списка с одним элементом
        """
        test_arr = [1]
        rand_val = 1
        rand_val_i = test_arr.index(rand_val)
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)

        test_arr.remove(rand_val)

        dyn_array.delete(rand_val_i)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], dyn_array[i])

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_empty_list(self):
        """
        Попытка удаления значения из пустого списка (проверка генерации IndexError)
        """
        test_arr = []
        rand_val_i = 2
        dyn_array = DynArray()
        with self.assertRaises(IndexError):
            dyn_array.delete(rand_val_i)

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_first_value_many_vals(self):
        """
        Удаление первого значения из списка (без изменения буфера)
        """
        test_arr = list(range(10))
        rand_val = 0
        rand_val_i = 0
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)

        test_arr.remove(rand_val)

        dyn_array.delete(rand_val_i)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], dyn_array[i])

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_mid_value_many_vals(self):
        """
        Удаление серединного значения из списка (без изменения буфера)
        """
        test_arr = list(range(10))
        rand_val = 4
        rand_val_i = 4
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)

        test_arr.remove(rand_val)

        dyn_array.delete(rand_val_i)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], dyn_array[i])

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_last_value_many_vals(self):
        """
        Удаление последнего значения из списка (без изменения буфера)
        """
        test_arr = list(range(10))
        rand_val = 9
        rand_val_i = 9
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)

        test_arr.remove(rand_val)

        dyn_array.delete(rand_val_i)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], dyn_array[i])

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_inserting_out_of_bounds(self):
        """
        Попытка вставки значения с индексом превышающим число элементов (проверка генерации IndexError)
        """
        test_arr = [1, 2, 3]
        length = len(test_arr)
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)

        with self.assertRaises(IndexError):
            dyn_array.insert(length + 1, 1)  # длина списка + 1

        self.assertEqual(len(dyn_array), len(test_arr))
        self.assertEqual(dyn_array.capacity, 16)

    def test_inserting_with_resizing_capacity(self):
        """
        Вставка значения, после которого должен измениться буфер
        """

        list_length = 16
        test_arr = list(range(list_length))

        dyn_array = DynArray()
        for item in test_arr:
            dyn_array.append(item)

        # append корректно работает
        self.assertEqual(dyn_array.capacity, 16)

        # делаем вставку в случайное место
        test_arr.insert(list_length - 2, list_length)
        dyn_array.insert(list_length - 2, list_length)

        # проверяем что сама вставка прошла корректно и последовательность идентична
        for i in range(len(test_arr)):
            self.assertEqual(dyn_array[i], test_arr[i])

        # длины списков совпадают (не обязательно, т.к. ошибка была бы на предыдущем шаге)
        self.assertEqual(len(dyn_array), len(test_arr))
        # буфер изменился в 2 раза
        self.assertEqual(dyn_array.capacity, 32)

    def test_inserting_without_resizing_capacity(self):
        """
        Вставка значения, после которого должен измениться буфер
        """

        list_length = 14
        test_arr = list(range(list_length))

        dyn_array = DynArray()
        for item in test_arr:
            dyn_array.append(item)

        # append корректно работает
        self.assertEqual(dyn_array.capacity, 16)

        # делаем вставку в случайное место
        test_arr.insert(list_length - 2, list_length)
        dyn_array.insert(list_length - 2, list_length)

        # проверяем что сама вставка прошла корректно и последовательность идентична
        for i in range(len(test_arr)):
            self.assertEqual(dyn_array[i], test_arr[i])

        # длины списков совпадают (не обязательно, т.к. ошибка была бы на предыдущем шаге)
        self.assertEqual(len(dyn_array), len(test_arr))
        # буфер не изменился
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_with_resizing_capacity(self):
        """
        Удаление серединного значения из списка (с изменением буфера)
        """
        test_arr = list(range(17))  # делаем список из 17 значений (буфер будет 32)
        rand_val_i = 4  # случайный индекс для удаления
        deleted_values = 2  # сколько элементов нужно удалить чтобы буфер изменился (чтобы было менее половины от 32)
        dyn_array = DynArray()

        for item in test_arr:
            dyn_array.append(item)
        # буфер должен быть 32
        self.assertEqual(dyn_array.capacity, 32)

        # удаляем 2 значения из списков
        for i in range(deleted_values):
            test_arr.pop(rand_val_i)
            dyn_array.delete(rand_val_i)

        # списки должны быть равны
        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], dyn_array[i])
        # списки должны быть равны
        self.assertEqual(len(dyn_array), len(test_arr))
        # проверяем изменение размера списка
        self.assertEqual(dyn_array.capacity, int(32 / 1.5))


if __name__ == '__main__':
    unittest.main()
