class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node: BSTNode):
        self.Root = node

    def FindNodeByKey(self, key) -> BSTFind:
        bst_find = BSTFind()
        current_node = self.Root
        last_node = None

        while current_node is not None:
            last_node = current_node

            if key < current_node.NodeKey:
                current_node = current_node.LeftChild
            elif key > current_node.NodeKey:
                current_node = current_node.RightChild
            else:
                # Base case: the current key is equal to the search key
                bst_find.Node = current_node
                bst_find.NodeHasKey = True
                return bst_find

        # Base case: has reached the end, and parent_node is a leaf or None (if there are no root).
        bst_find.Node = last_node
        bst_find.NodeHasKey = False
        # Fill toLeft with a logical expression
        if last_node is not None:
            bst_find.ToLeft = key < last_node.NodeKey

        return bst_find

    def AddKeyValue(self, key, val) -> bool:
        bst_find = self.FindNodeByKey(key)

        # если ключ уже есть
        if bst_find.NodeHasKey:
            return False

        new_node = BSTNode(key, val, bst_find.Node)

        # If Root is None
        if bst_find.Node is None:
            # then the tree was empty, and new node becomes the root
            self.Root = new_node
        elif bst_find.ToLeft:
            # then add a new node as a left descendant
            bst_find.Node.LeftChild = new_node
        else:
            # then add a new node as a right descendant
            bst_find.Node.RightChild = new_node

        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        current_node = FromNode
        if FindMax:
            # Go down the right-hand child elements to the last one
            while current_node.RightChild is not None:
                current_node = current_node.RightChild
        else:
            # Go down the left-hand child elements to the last one
            while current_node.LeftChild is not None:
                current_node = current_node.LeftChild

        return current_node

    def DeleteNodeByKey(self, key):
        bst_find = self.FindNodeByKey(key)

        # if node doesn't found
        if not bst_find.NodeHasKey:
            return False

        node_to_delete = bst_find.Node
        parent_node = node_to_delete.Parent
        if node_to_delete.LeftChild and node_to_delete.RightChild:
            # Node has two descendants
            successor = self.FinMinMax(node_to_delete.RightChild, False)
            node_to_delete.NodeKey = successor.NodeKey  # Copy the successor key
            node_to_delete.NodeValue = successor.NodeValue  # Copy the successor value
            self.delete_node(successor)  # Remove the successor node
        elif node_to_delete.LeftChild or node_to_delete.RightChild:
            # A node has one descendant
            child = node_to_delete.LeftChild if node_to_delete.LeftChild else node_to_delete.RightChild
            if parent_node:
                if parent_node.LeftChild == node_to_delete:
                    parent_node.LeftChild = child
                else:
                    parent_node.RightChild = child
                child.Parent = parent_node
            else:
                self.Root = child
                child.Parent = None
        else:
            # The node has no descendants
            if parent_node:
                if parent_node.LeftChild == node_to_delete:
                    parent_node.LeftChild = None
                else:
                    parent_node.RightChild = None
            else:
                self.Root = None

        return True

    def delete_node(self, node):
        # This method removes a node that has exactly one or fewer descendants
        parent = node.Parent
        if node.LeftChild or node.RightChild:
            child = node.LeftChild if node.LeftChild else node.RightChild
            if parent:
                if parent.LeftChild == node:
                    parent.LeftChild = child
                else:
                    parent.RightChild = child
                child.Parent = parent
            else:
                self.Root = child
                child.Parent = None
        else:
            if parent:
                if parent.LeftChild == node:
                    parent.LeftChild = None
                else:
                    parent.RightChild = None
            else:
                self.Root = None

    def Count(self):
        if self.Root is None:
            return 0
        stack = [self.Root]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if node.LeftChild:
                stack.append(node.LeftChild)
            if node.RightChild:
                stack.append(node.RightChild)
        return count
