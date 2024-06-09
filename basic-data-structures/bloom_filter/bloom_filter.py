class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1: str) -> int:
        n = 17
        value = 0
        for c in str1:
            code = ord(c)
            value = (value * n + code) % self.filter_len
        return value

    def hash2(self, str1: str) -> int:
        n = 223
        value = 0
        for c in str1:
            code = ord(c)
            value = (value * n + code) % self.filter_len
        return value

    def add(self, str1: str):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        self.filter |= (1 << index1)
        self.filter |= (1 << index2)

    def is_value(self, str1: str) -> bool:
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        bit_set_1 = (self.filter & (1 << index1)) != 0
        bit_set_2 = (self.filter & (1 << index2)) != 0
        return bit_set_1 and bit_set_2
