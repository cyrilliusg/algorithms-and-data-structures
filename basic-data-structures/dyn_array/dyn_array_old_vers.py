import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        if i == self.count:
            self.append(itm)
            return

        for curr_i in reversed(range(i, self.count)):
            self.array[curr_i + 1] = self.array[curr_i]

        self.array[i] = itm
        self.count += 1

        return

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        if self.count - 1 < self.capacity / 2:
            new_size = int(self.capacity / 1.5)
            self.resize(16 if new_size < 16 else new_size)

        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]

        self.count -= 1

        return

    
