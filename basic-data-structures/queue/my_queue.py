from typing import Union, Any


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Any):
        self.queue.append(item)

    def dequeue(self) -> Union[Any, None]:
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self) -> int:
        return len(self.queue)
