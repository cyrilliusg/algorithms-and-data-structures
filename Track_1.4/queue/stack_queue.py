from typing import Union, Any


class StackQueue:
    def __init__(self):
        # Инициализируем два стека
        self.in_stack = Stack()  # для внесения значений
        self.out_stack = Stack()  # для выдачи значений

    def enqueue(self, item):
        self.in_stack.push(item)  # Просто добавляем элемент в "входной" стек

    def dequeue(self):
        # Если "выходной" стек пуст, перекладываем все элементы из "входного" стека в "выходной"
        if self.out_stack.size() == 0:
            while self.in_stack.size() > 0:
                self.out_stack.push(self.in_stack.pop())
        # Возвращаем верхний элемент из "выходного" стека
        return self.out_stack.pop()

    def size(self):
        # Размер очереди равен сумме размеров обоих стеков
        return self.in_stack.size() + self.out_stack.size()


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
