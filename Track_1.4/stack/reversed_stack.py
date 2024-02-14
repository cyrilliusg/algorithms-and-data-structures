from typing import Union, Any
from stack import Stack


class ReversedStack(Stack):
    def __init__(self):
        super().__init__()

    def pop(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value: Any):
        self.stack.insert(0, value)

    def peek(self) -> Union[None, Any]:
        if self.size() > 0:
            return self.stack[0]
        return None
