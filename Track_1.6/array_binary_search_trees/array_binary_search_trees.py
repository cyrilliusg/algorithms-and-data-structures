class aBST:
    def __init__(self, depth):
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size

    def FindKeyIndex(self, key):
        index = 0
        if self.Tree[index] is None:
            return index
        while index < self.tree_size:
            if self.Tree[index] is None:
                return -index  # Return a negative index for a free position
            elif self.Tree[index] == key:
                return index  # Key found, return index
            elif key < self.Tree[index]:
                index = 2 * index + 1  # Step up to the left descendant
            else:
                index = 2 * index + 2  # Step up to the right descendant
        return None  # The tree is fully populated, no key found

    def AddKey(self, key):
        index = self.FindKeyIndex(key)

        if index is None or index > 0:
            return
        if index == 0:
            self.Tree[index] = key
        else:
            self.Tree[-index] = key
