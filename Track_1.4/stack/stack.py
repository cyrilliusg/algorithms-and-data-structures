from typing import Union


class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self) -> Union[None, any]:
        value = None

        if self.size() > 0:
            value = self.stack[0]
            self.stack = self.stack[1:]

        return value

    def push(self, value: any):
        self.stack.append(value)

    def peek(self) -> Union[None, any]:
        value = None
        if self.size() > 0:
            value = self.stack[0]

        return value
