class PowerSet:
    def __init__(self):
        self.storage = {}

    def size(self):
        return len(self.storage)

    def put(self, value):
        self.storage[value] = True

    def get(self, value):
        return value in self.storage

    def remove(self, value):
        if value in self.storage:
            del self.storage[value]
            return True
        return False

    def intersection(self, set2):
        smallest_set = set2 if set2.size() <= self.size() else self
        biggest_set = set2 if set2.size() >= self.size() else self
        result_set = PowerSet()
        for item in smallest_set.storage:
            if item is not None and biggest_set.get(item):
                result_set.put(item)
        return result_set  # if result_set.size() > 0 else None

    def union(self, set2):
        result_set = PowerSet()
        for power_set in [self, set2]:
            for item in power_set.storage:
                if item is not None:
                    result_set.put(item)
        return result_set  # if result_set.size() > 0 else None

    def difference(self, set2):
        result_set = PowerSet()
        for item in self.storage:
            if item is not None and not set2.get(item):
                result_set.put(item)
        return result_set

    def issubset(self, set2):
        for item in set2.storage:
            if item is not None and not self.get(item):
                return False
        return True
