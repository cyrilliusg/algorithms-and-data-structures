class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str) -> int:
        x = len(value.encode('utf-8'))  # string size in bytes
        p = 5  # prime number
        a = 3  # coefficient a
        b = 2  # coefficient b
        return (a * x + b) % p % self.size

    def seek_slot(self, value: str) -> None | int:
        slot_index = self.hash_fun(value)
        original_slot_index = slot_index
        while self.slots[slot_index] is not None:
            slot_index += + self.step  # step up
            if slot_index >= self.size:  # if out of bounds
                slot_index = slot_index - self.size  # round the step
            if slot_index == original_slot_index:
                return None
        return slot_index

    def put(self, value: str) -> None | int:
        slot_index = self.seek_slot(value)

        if slot_index is not None:
            self.slots[slot_index] = value
            return slot_index
        return None

    def find(self, value: str) -> None | int:
        for i in range(self.size):
            if self.slots[i] == value:
                return i
        return None
