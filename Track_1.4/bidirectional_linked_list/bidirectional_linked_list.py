class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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

        current_node = self.head
        while current_node is not None:
            if current_node.value == val:
                if current_node == self.head:  # if the value is the first
                    self.head = current_node.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None  # The list went blank
                elif current_node == self.tail:  # if the last one
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev

                if not all:
                    break
            current_node = current_node.next

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
        if afterNode is None:  # problem statement
            if self.head is None:  # if the list is empty
                self.add_in_head(newNode)  # then put it at the beginning
            else:
                # if it's not empty, put it in the end
                self.tail.next, newNode.prev = newNode, self.tail
                self.tail = newNode
        else:
            # if there is an afternode, then if afternode is an end
            if self.tail == afterNode:
                # то аналогично как выше
                self.tail.next, newNode.prev = newNode, self.tail
                self.tail = newNode
            else:
                # otherwise if to any other value (we do not allow the list to be empty)
                newNode.next, afterNode.next, newNode.prev = afterNode.next, newNode, afterNode
                newNode.next.prev = newNode

        return

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next, self.head.prev = self.head, newNode
            self.head = newNode
