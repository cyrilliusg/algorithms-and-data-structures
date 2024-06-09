import unittest
from my_queue import Queue
from stack_queue import StackQueue


class UnitTestQueue(unittest.TestCase):
    """
    Тест методов очереди

    Рассмотрим следующие случаи:
    -- тестирование enqueue
    -- тестирование dequeue
    В Обычной очереди и очереди из 2-х Стэков
    С пустой очередью, очередью из 1 элемента и множества элементов
    """

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('first')
        self.assertEqual(queue.size(), 1)
        self.assertIn('first', queue.queue)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('first')
        queue.enqueue('second')
        dequeued = queue.dequeue()
        self.assertEqual(dequeued, 'first')
        self.assertEqual(queue.size(), 1)
        self.assertNotIn('first', queue.queue)

    def test_empty_dequeue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.size(), 0)

    def test_stack_enqueue(self):
        queue = StackQueue()
        queue.enqueue('first')
        queue.enqueue('second')
        self.assertEqual(queue.size(), 2)

    def test_stack_dequeue(self):
        queue = StackQueue()
        queue.enqueue('first')
        queue.enqueue('second')
        dequeued_item = queue.dequeue()
        self.assertEqual(dequeued_item, 'first')
        self.assertEqual(queue.size(), 1)
        # Ensure FIFO order is maintained
        dequeued_item = queue.dequeue()
        self.assertEqual(dequeued_item, 'second')
        self.assertEqual(queue.size(), 0)

    def test_stack_empty_dequeue(self):
        queue = StackQueue()
        # Test dequeue on empty queue
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.size(), 0)

    def test_stack_mixed_operations(self):
        queue = StackQueue()
        # Mix of enqueue and dequeue operations to test internal state
        queue.enqueue('first')
        queue.enqueue('second')
        self.assertEqual(queue.dequeue(), 'first')
        queue.enqueue('third')
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), 'second')
        self.assertEqual(queue.dequeue(), 'third')
        self.assertEqual(queue.size(), 0)


if __name__ == '__main__':
    unittest.main()
