from typing import Union, Any


class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack.pop()
        return None

    def push(self, value: Any):
        self.stack.append(value)

    def peek(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack[-1]
        return None
