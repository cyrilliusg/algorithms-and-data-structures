from typing import Any, Optional

class BoundedStack:
    def __init__(self, capacity: int = 32) -> None:
        """
        Конструктор BoundedStack.
        :param capacity: максимально допустимое количество элементов в стеке (должно быть > 0).
                         Если параметр не задан, используется значение 32.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.stack = []  # внутреннее хранилище элементов стека

    def size(self) -> int:
        """Возвращает текущее количество элементов в стеке."""
        return len(self.stack)

    def push(self, value: Any) -> None:
        """
        Добавляет элемент на верх стека.
        :raises OverflowError: если достигнут предел емкости стека.
        """
        if self.size() >= self.capacity:
            raise OverflowError("Stack capacity reached")
        self.stack.append(value)

    def pop(self) -> Optional[Any]:
        """
        Удаляет и возвращает верхний элемент стека.
        Если стек пустой, возвращается None.
        """
        if self.size() > 0:
            return self.stack.pop()
        return None

    def peek(self) -> Optional[Any]:
        """
        Возвращает верхний элемент стека, не удаляя его.
        Если стек пустой, возвращается None.
        """
        if self.size() > 0:
            return self.stack[-1]
        return None

    def clear(self) -> None:
        """Очищает стек, удаляя все его элементы."""
        self.stack.clear()
