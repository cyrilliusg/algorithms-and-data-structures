class aBST:
    def __init__(self, depth):
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            current_key = self.Tree[index]
            if current_key is None:
                return -(index + 1)
            if current_key == key:
                return index
            elif key < current_key:
                index = 2 * index + 1
            else:
                index = 2 * index + 2
        return None

    def AddKey(self, key):
        index = 0
        while index < len(self.Tree):
            current_key = self.Tree[index]
            if current_key is None:
                self.Tree[index] = key
                return index
            elif key == current_key:
                return index
            elif key < current_key:
                index = 2 * index + 1
            else:
                index = 2 * index + 2
        return -1  # If tree is full
