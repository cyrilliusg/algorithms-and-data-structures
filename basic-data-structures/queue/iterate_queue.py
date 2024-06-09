from queue import Queue


def rotate_queue(queue: Queue, n: int):
    size = queue.size()
    for _ in range(n):
        item = queue.dequeue()
        queue.enqueue(item)
