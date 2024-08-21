class BinarySearch:
    def __init__(self, sorted_array: list[int]):
        self.array: list[int] = sorted_array
        self.Left = 0
        self.Right = len(sorted_array) - 1
        self.result = None

    def Step(self, N: int):
        if self.result is not None:
            return

        if self.Left > self.Right:
            self.result = False
            return True

        middle_index = (self.Left + self.Right) // 2

        if self.array[middle_index] == N:
            self.result = True
            return

        if self.array[middle_index] < N:
            self.Left = middle_index + 1
        elif self.array[middle_index] > N:
            self.Right = middle_index - 1

    def GetResult(self) -> int:
        if self.result is None:
            return 0
        elif self.result:
            return 1
        else:
            return -1
