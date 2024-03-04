from typing import Any


class NativeDictionary:
    def __init__(self, sz: int):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key: str) -> int:
        a = 2  # coefficient a
        b = 3  # coefficient b
        length = len(key.encode('utf-8'))  # string size in bytes
        p = 17  # prime number
        return (a * length + b) % p % self.size

    def put(self, key: str, value: Any):
        slot_index = self.hash_fun(key)
        step = 3
        while self.slots[slot_index] is not None and self.slots[slot_index] != key:
            slot_index += step  # step up
            if slot_index >= self.size:  # if out of bounds
                slot_index = slot_index - self.size  # round the step

        self.slots[slot_index] = key
        self.values[slot_index] = value

    def is_key(self, key: str) -> bool:
        step = 3
        slot_index = self.hash_fun(key)
        while self.slots[slot_index] is not None:
            if self.slots[slot_index] == key:
                return True
            slot_index += step  # step up
        return False

    def get(self, key: str) -> Any:
        step = 3
        slot_index = self.hash_fun(key)
        while self.slots[slot_index] is not None:
            if self.slots[slot_index] == key:
                return self.values[slot_index]
            slot_index += step  # step up
        return None
