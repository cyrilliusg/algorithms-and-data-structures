class aBST:
    def __init__(self, depth):
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size

    def FindKeyIndex(self, key):
        index = 0
        last_possible_index = -1
        while index < len(self.Tree):
            current_key = self.Tree[index]
            if current_key is None:
                if last_possible_index == -1:  # Remember first encountered None
                    last_possible_index = index
                break  # Break if node is empty
            if current_key == key:
                return index  # Return index of found key
            elif key < current_key:
                index = 2 * index + 1
            else:
                index = 2 * index + 2
        # Return negative index if key not found
        return -(last_possible_index + 1) if last_possible_index != -1 else None

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
