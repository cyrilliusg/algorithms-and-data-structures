from queue import Queue


def rotate_queue(queue: Queue, n: int):
    size = queue.size()
    # Ограничиваем n размером очереди, чтобы избежать лишних операций
    n = n % size if size > 0 else 0
    for _ in range(n):
        item = queue.dequeue()
        queue.enqueue(item)
