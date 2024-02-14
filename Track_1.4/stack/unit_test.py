import unittest
from stack import Stack, ReversedStack
import random


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

    def test_push(self):
        """
        Проверка внесения значений
        """
        stack = Stack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        test_arr.reverse()

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.stack[i])

        self.assertEqual(len(test_arr), len(stack.stack))

    def test_pop(self):
        """
        Проверка внесения значений
        """
        stack = Stack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.pop())

        self.assertEqual(0, len(stack.stack))

    def test_peek(self):
        """
        Проверка внесения значений
        """
        stack = Stack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.peek())
            stack.pop()

        self.assertEqual(0, len(stack.stack))

    def test_reversed_push(self):
        """
        Проверка внесения значений
        """
        stack = ReversedStack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.stack[i])

        self.assertEqual(len(test_arr), len(stack.stack))

    def test_reversed_pop(self):
        """
        Проверка внесения значений
        """
        stack = ReversedStack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.pop())

        self.assertEqual(0, len(stack.stack))

    def test_reversed_peek(self):
        """
        Проверка внесения значений
        """
        stack = ReversedStack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.peek())
            stack.pop()

        self.assertEqual(0, len(stack.stack))


if __name__ == '__main__':
    unittest.main()
