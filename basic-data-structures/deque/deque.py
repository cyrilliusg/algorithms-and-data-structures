from typing import Union, Any


class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item: Any):
        self.deque.append(item)

    def addTail(self, item: Any):
        self.deque.insert(0, item)

    def removeFront(self) -> Union[Any, None]:
        if self.size() != 0:
            return self.deque.pop()
        return None

    def removeTail(self) -> Union[Any, None]:
        if self.size() != 0:
            return self.deque.pop(0)
        return None

    def size(self) -> int:
        return len(self.deque)
