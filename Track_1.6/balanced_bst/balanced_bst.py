class BSTNode:
    def __init__(self, key, parent=None):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:
    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if not a:
            return
        a.sort()
        self.Root = self._generate_tree_recursive(a, 0, len(a) - 1, None)

    def _generate_tree_recursive(self, sorted_array, start, end, parent):
        if start > end:
            return None

        mid = start + (end - start) // 2
        node = BSTNode(sorted_array[mid], parent)
        if parent is None:
            node.Level = 0
        else:
            node.Level = parent.Level + 1

        node.LeftChild = self._generate_tree_recursive(sorted_array, start, mid - 1, node)
        node.RightChild = self._generate_tree_recursive(sorted_array, mid + 1, end, node)

        return node

    def IsBalanced(self, root_node):
        def check_balance(node):
            if not node:
                return 0, True

            left_height, left_balanced = check_balance(node.LeftChild)
            right_height, right_balanced = check_balance(node.RightChild)

            current_height = max(left_height, right_height) + 1
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return current_height, is_balanced

        _, balanced = check_balance(root_node)
        return balanced
