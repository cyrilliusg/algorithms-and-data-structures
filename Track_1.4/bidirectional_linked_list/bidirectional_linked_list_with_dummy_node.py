from bidirectional_linked_list import Node


class Dummy:

    def __init__(self):
        self.head = Node(None)  # dummy head
        self.tail = Node(None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev  # actual tail node
        item.next = self.tail  # dummy node
        self.tail.prev.next = item  # from penultimate to tail
        self.tail.prev = item  # new actual tail node

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def delete(self, value, all=False):
        current_node = self.head.next
        while current_node != self.tail:
            if current_node.value == value:
                current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
                if not all:
                    break
            current_node = current_node.next

    def find(self, val):
        node = self.head.next
        while node != self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head.next
        while node != self.tail:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def clean(self):
        self.head.next = None
        self.tail.next = None

    def len(self):
        length = 0
        node = self.head.next
        while node != self.tail:
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
        newNode.next, self.head.next.prev = self.head.next, newNode
        self.head = newNode