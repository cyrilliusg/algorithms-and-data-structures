class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.Level = 0  # depth level

    def AssignLevel(self):
        queue = [(self, self.Parent.Level + 1)]  # Let's use queue pairs of node and it's level

        while queue:
            current_node, level = queue.pop()
            current_node.Level = level
            for child in current_node.Children:
                queue.append((child, level + 1))

    def __repr__(self):
        return f'value: {self.NodeValue} - level: {self.Level}'


class SimpleTree:

    def __init__(self, root: SimpleTreeNode):
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        NewChild.AssignLevel()  # Assign new level for current node and it's child's
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        # Do not delete root node
        if NodeToDelete == self.Root or NodeToDelete.Parent is None:
            return

        if NodeToDelete in NodeToDelete.Parent.Children:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        all_nodes = []

        if self.Root is None:
            return all_nodes
        stack = [self.Root]  # Let's use stack for iterate through tree in depth
        while stack:
            current_node = stack.pop()
            all_nodes.append(current_node)
            for child in current_node.Children:
                stack.append(child)
        return all_nodes

    def FindNodesByValue(self, val):
        result = []
        if self.Root is None:
            return result

        stack = [self.Root]
        while stack:
            current_node = stack.pop()
            if current_node.NodeValue == val:
                result.append(current_node)
            stack.extend(current_node.Children)
        return result

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        if OriginalNode == self.Root or OriginalNode.Parent is None:
            return
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        total_count = 0

        if self.Root is None:
            return total_count

        stack = [self.Root]

        while stack:
            current_node = stack.pop()
            total_count += 1
            stack.extend(current_node.Children)

        return total_count

    def LeafCount(self):
        total_count = 0

        if self.Root is None:
            return total_count

        stack = [self.Root]

        while stack:
            current_node = stack.pop()
            total_count += 1 if not current_node.Children else 0
            stack.extend(current_node.Children)

        return total_count

    def AssignLevel(self):
        if self.Root is None:
            return

        queue = [(self.Root, 0)]  # Let's use queue pairs of node and it's level

        while queue:
            current_node, level = queue.pop()
            current_node.Level = level
            for child in current_node.Children:
                queue.append((child, level + 1))
