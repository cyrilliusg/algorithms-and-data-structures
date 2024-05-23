class Heap:

    def __init__(self):
        self.HeapArray = []  # non-negative keys - numbers
        self.size = 0  # current heap size
        self.capacity = 0  # max heap capacity

    def MakeHeap(self, a, depth):
        self.capacity = 2 ** (depth + 1) - 1  # maximum array size for a heap of a given depth
        self.HeapArray = [None] * self.capacity
        for key in a:
            self.Add(key)

    def GetMax(self):
        if self.size == 0:
            return -1  # if heap is empty
        max_value = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.size - 1]
        self.HeapArray[self.size - 1] = None
        self.size -= 1
        self._siftDown(0)
        return max_value

    def Add(self, key):
        if self.size >= self.capacity:
            return False  # if heap is full
        self.HeapArray[self.size] = key
        self.size += 1
        self._siftUp(self.size - 1)
        return True

    def _siftUp(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.HeapArray[parent] < self.HeapArray[index]:
            self.HeapArray[parent], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent]
            index = parent
            parent = (index - 1) // 2

    def _siftDown(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.HeapArray[left] is not None and self.HeapArray[left] > self.HeapArray[largest]:
            largest = left
        if right < self.size and self.HeapArray[right] is not None and self.HeapArray[right] > self.HeapArray[largest]:
            largest = right
        if largest != index:
            self.HeapArray[index], self.HeapArray[largest] = self.HeapArray[largest], self.HeapArray[index]
            self._siftDown(largest)
