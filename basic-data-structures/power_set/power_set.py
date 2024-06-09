class HashTable:
    def __init__(self, sz, stp):
        self.capacity = sz
        self.step = stp
        self.slots = [None] * self.capacity

    def hash_fun(self, value: str) -> int:
        x = len(value.encode('utf-8'))  # string size in bytes
        p = 5  # prime number
        a = 3  # coefficient a
        b = 2  # coefficient b
        return (a * x + b) % p % self.capacity

    def seek_slot(self, value: str) -> None | int:
        slot_index = self.hash_fun(value)
        original_slot_index = slot_index
        while self.slots[slot_index] is not None:
            slot_index += + self.step  # step up
            if slot_index >= self.capacity:  # if out of bounds
                slot_index = slot_index - self.capacity  # round the step
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
        start_slot = self.hash_fun(value)
        slot = start_slot

        while self.slots[slot] is not None:
            if self.slots[slot] == value:
                return slot
            slot += + self.step  # step up
            if slot >= self.capacity:  # if out of bounds
                slot = slot - self.capacity  # round the step
            if slot == start_slot:
                break
        return None


class PowerSet(HashTable):
    def __init__(self, sz=17, step=3):
        super().__init__(sz, step)
        self.count = 0  # for avoiding linear complexity

    def size(self):
        return self.count

    def put(self, value):
        if not self.get(value):
            if self.count == self.capacity:
                self._resize(
                    self._get_next_prime(2 * self.capacity))
            super().put(value)
            self.count += 1
            return True
        return False

    def get(self, value):
        return super().find(value) is not None

    def remove(self, value):
        slot_index = super().find(value)
        if slot_index is not None:
            if self.count - 1 < self.capacity / 2:
                new_size = self._get_next_prime(int(self.capacity / 1.5))
                self._resize(17 if new_size < 17 else new_size)

            self.slots[slot_index] = None
            self.count -= 1
            return True
        return False

    def intersection(self, set2):
        smallest_set = set2 if set2.size() <= self.count else self
        biggest_set = set2 if set2.size() >= self.count else self
        result_set = PowerSet()
        for item in smallest_set.slots:
            if item is not None and biggest_set.get(item):
                result_set.put(item)
        return result_set  # if result_set.size() > 0 else None

    def union(self, set2):
        result_set = PowerSet()
        for power_set in [self, set2]:
            for item in power_set.slots:
                if item is not None:
                    result_set.put(item)
        return result_set  # if result_set.size() > 0 else None

    def difference(self, set2):
        result_set = PowerSet()
        for item in self.slots:
            if item is not None and not set2.get(item):
                result_set.put(item)
        return result_set

    def issubset(self, set2):
        for item in set2.slots:
            if item is not None and not self.get(item):
                return False
        return True

    def _resize(self, new_size):
        old_slots = self.slots
        self.capacity = new_size
        self.slots = [None] * self.capacity
        self.count = 0

        for item in old_slots:
            if item is not None:
                self.put(item)

    def _get_next_prime(self, n):
       
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n
