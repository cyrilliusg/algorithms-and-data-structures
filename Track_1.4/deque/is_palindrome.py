from deque import Deque


def is_palindrome(row: str) -> bool:
    deque = Deque()
    for char in row:
        deque.addFront(char)

    tail = deque.removeTail()
    front = deque.removeFront()
    while tail is not None and front is not None:
        if tail != front:
            return False
        tail = deque.removeTail()
        front = deque.removeFront()
    return True
