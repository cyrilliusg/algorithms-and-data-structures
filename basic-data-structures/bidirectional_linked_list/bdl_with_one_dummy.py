from bidirectional_linked_list import Node


class Dummy:

    def __init__(self):
        self.dummy = Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def add_in_tail(self, item):
        item.prev = self.dummy.prev
        item.next = self.dummy
        self.dummy.prev.next = item
        self.dummy.prev = item

    def print_all_nodes(self):
        node = self.dummy
        while node != self.dummy:
            print(node.value)
            node = node.next

    def delete(self, value, all=False):
        current_node = self.dummy.next
        while current_node != self.dummy:
            if current_node.value == value:
                current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
                if not all:
                    break
            current_node = current_node.next

    def find(self, val):
        node = self.dummy.next
        while node != self.dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.dummy.next
        while node != self.dummy:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def clean(self):
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def len(self):
        length = 0
        node = self.dummy.next
        while node != self.dummy:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:  # problem statement
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.next.prev = newNode
        return

    def add_in_head(self, newNode):
        newNode.next, self.dummy.next.next.prev = self.dummy.next.next, newNode
        self.dummy.next = newNode
