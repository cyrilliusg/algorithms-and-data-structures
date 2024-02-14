from typing import Union, Any


class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack.pop()  # Удаляет и возвращает последний элемент списка
        return None

    def push(self, value: Any):
        self.stack.append(value)  # Добавляет элемент в конец списка

    def peek(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack[-1]  # Возвращает последний элемент списка без его удаления
        return None
