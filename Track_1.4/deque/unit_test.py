import unittest
import random
from deque import Deque


class UnitTestDeque(unittest.TestCase):
    """
    Тест методов двусторонней очереди

    Рассмотрим следующие случаи:
    -- тестирование removeFront
    -- тестирование removeTail
    -- тестирование addFront
    -- тестирование addTail
    В Обычной очереди и очереди из 2-х Стэков
    С пустой очередью, очередью из 1 элемента и множества элементов
    """

    def test_addFront(self):
        deque = Deque()
        deque.addFront('first')
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.deque[-1], 'first')

    def test_addTail(self):
        deque = Deque()
        deque.addTail('last')
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.deque[0], 'last')

    def test_removeFront(self):
        deque = Deque()
        deque.addFront('first')
        deque.addTail('last')
        self.assertEqual(deque.removeFront(), 'first')
        self.assertEqual(deque.size(), 1)
        self.assertNotIn('first', deque.deque)

    def test_removeTail(self):
        deque = Deque()
        deque.addFront('first')
        deque.addTail('last')
        self.assertEqual(deque.removeTail(), 'last')
        self.assertEqual(deque.size(), 1)
        self.assertNotIn('last', deque.deque)


if __name__ == '__main__':
    unittest.main()
