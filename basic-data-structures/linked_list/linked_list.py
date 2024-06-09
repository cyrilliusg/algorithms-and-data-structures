class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if self.head is None:
            return

        # if all values in list are same and flag is True
        while self.head and self.head.value == val:
            self.head = self.head.next
            if not all:  # If we delete only first value
                if self.head is None:  # If after deleting the list is empty
                    self.tail = None
                return
            if self.head is None:
                self.tail = None
                return

        node = self.head
        previous_node = None
        while node is not None:
            if node.value == val:
                if node.next is None:  # If we delete last value
                    previous_node.next = None
                    self.tail = previous_node  # Update tail if deleted last value
                    if not all:  # If we need to delete only one value
                        break
                else:
                    previous_node.next = node.next

                if not all:  # If we need to delete only one value
                    break
            else:
                previous_node = node

            node = node.next

        # If after deleting there are one element then update tail
        if self.head and self.head.next is None:
            self.tail = self.head

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            # put first
            newNode.next, self.head = self.head, newNode
            if self.tail is None:  # If the list was empty, then we update tail
                self.tail = newNode
        else:
            newNode.next, afterNode.next = afterNode.next, newNode
            if afterNode == self.tail:  # If we inserted after the last node, then update tail
                self.tail = newNode

        return
