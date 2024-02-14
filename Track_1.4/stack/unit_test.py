import unittest
from reversed_stack import Stack, ReversedStack
import random


class UnitTestDynArray(unittest.TestCase):
    """
    Тест методов стэка

    Рассмотрим следующие случаи:
    -- тестирование push
    -- тестирование pop
    -- тестирование peek
    В Обычном и Реверснутом стэке
    """

    def test_push(self):
        """
        Проверка внесения значений
        """
        stack = Stack()
        test_arr = random.sample(range(-10, 30), 10)

        for item in test_arr:
            stack.push(item)

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

        test_arr.reverse()
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

        test_arr.reverse()

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

        test_arr.reverse()

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
        test_arr.reverse()
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
        test_arr.reverse()
        for i in range(len(test_arr)):
            self.assertEqual(test_arr[i], stack.peek())
            stack.pop()

        self.assertEqual(0, len(stack.stack))


if __name__ == '__main__':
    unittest.main()
