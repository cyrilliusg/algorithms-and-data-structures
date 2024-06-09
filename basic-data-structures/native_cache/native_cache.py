class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

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
            slot_index += + 3  # step up
            if slot_index >= self.size:  # if out of bounds
                slot_index = slot_index - self.size  # round the step
            if slot_index == original_slot_index:
                return None
        return slot_index

    def put(self, value: str) -> None | int:
        slot_index = self.seek_slot(value)

        if slot_index is None:  # if table is full
            smallest_index = self.find_smallest()
            self.slots[smallest_index] = None
            self.values[smallest_index] = None
            self.hits[smallest_index] = 0
            self.put(value)  # recursive calling 'put' method for putting value using collision resolution mechanism
        else:
            self.slots[slot_index] = value
            self.hits[slot_index] += 1
            return slot_index

    def find_smallest(self) -> int:
        return self.hits.index(min(self.hits))

    def find(self, value: str) -> None | int:
        start_slot = self.hash_fun(value)
        slot = start_slot

        while self.slots[slot] is not None:
            if self.slots[slot] == value:
                return slot
            slot += + 3  # step up
            if slot >= self.size:  # if out of bounds
                slot = slot - self.size  # round the step
            if slot == start_slot:
                break
        return None

    def get(self, value):
        index = self.find(value)
        if index is None:
            return None
        return self.values[index]
