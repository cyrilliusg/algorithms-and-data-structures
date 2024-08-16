class BinarySearch:
    def __init__(self, sorted_array: list[int]):
        self.array: list[int] = sorted_array
        self.L = 0
        self.R = len(sorted_array) - 1
        self.result = None

    def Step(self, N: int):
        if self.result is not None:
            return

        if self.L > self.R:
            self.result = False
            return True

        middle_index = (self.L + self.R) // 2

        if self.array[middle_index] == N:
            self.result = True
            return

        if self.array[middle_index] < N:
            self.L = middle_index + 1
        elif self.array[middle_index] > N:
            self.R = middle_index - 1

    def GetResult(self) -> int:
        if self.result is None:
            return 0
        elif self.result:
            return 1
        else:
            return -1
