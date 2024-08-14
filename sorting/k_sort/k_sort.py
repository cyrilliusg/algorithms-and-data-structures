class ksort:
    def __init__(self):
        # 8 letters (a-h) and 100 numbers (00-99)
        self.items = [None] * 800

    def index(self, s: str) -> int:
        # check row for correct format
        if len(s) != 3:
            return -1
        if not ('a' <= s[0] <= 'h'):
            return -1
        if not (s[1:].isdigit() and len(s[1:]) == 2):
            return -1

        # calculate index
        letter_index = ord(s[0]) - ord('a')  # a = 0, b = 1, ..., h = 7
        number_index = int(s[1:])  # MN as an integer

        return letter_index * 100 + number_index

    def add(self, s: str) -> bool:
        idx = self.index(s)
        if idx == -1:
            return False

        self.items[idx] = s
        return True
