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

        node = self.head
        previous_node = None

        while node is not None:
            if node.value == val:
                # if last value
                if node.next is None:
                    # if first value
                    if previous_node is None:
                        # The list becomes empty
                        self.head = None
                        self.tail = None
                    else:
                        # if middle or last value
                        previous_node.next = None  # Update tail
                        self.tail = previous_node
                else:
                    # if first value
                    if previous_node is None:
                        self.head = node.next  # then we set the second value in the head
                    else:
                        # if middle or last value
                        previous_node.next = node.next

                if not all:
                    break

                if previous_node is None:
                    # if first value
                    node = self.head  # then the new node will be the head
                else:
                    # if middle or last value
                    node = previous_node.next  # otherwise the new node becomes the following value

            else:
                # if don't equal to desired
                previous_node, node = node, node.next  # previous becomes current, current becomes next

        if self.tail and self.tail.value == val:
            self.tail = previous_node

    def clean(self):
        if self.head is None:
            return

        while self.head is not None:
            next_node = self.head.next
            del self.head
            self.head = next_node

    def len(self):
        if self.head is None:
            return 0

        node = self.head
        length = 1

        while node is not None:
            next_node = node.next

            if next_node is None:
                return length
            else:
                length += 1
                node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            # put first
            newNode.next, self.head = self.head, newNode
        else:
            newNode.next, afterNode.next = afterNode.next, newNode

        return
