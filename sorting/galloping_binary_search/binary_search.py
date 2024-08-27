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

        if self.Left == self.Right or self.Left == self.Right - 1:
            if self.array[self.Left] == N or (self.Left != self.Right and self.array[self.Right] == N):
                self.result = True
            else:
                self.result = False

    def GetResult(self) -> int:
        if self.result is None:
            return 0
        elif self.result:
            return 1
        else:
            return -1

    def GallopingSearch(self, sorted_array: list[int], target: int) -> bool:
        self.array = sorted_array
        if not sorted_array:
            return False
        i = 1
        current_index = 0

        while i < len(sorted_array):
            if sorted_array[current_index] == target:
                return True

            if sorted_array[current_index] < target:
                i += 1
                new_index = 2 ** i - 2
                if new_index < len(sorted_array):
                    current_index = new_index
                    continue
                else:
                    current_index = len(sorted_array) - 1
                    break

            else:
                lower_bound = (2 ** (i - 1) - 2) + 1
                upper_bound = current_index

                self.Left = lower_bound
                self.Right = upper_bound
                while self.GetResult() == 0:
                    self.Step(target)
                return self.GetResult() == 1

        return self.array[current_index] == target