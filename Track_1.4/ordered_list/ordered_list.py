class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1: int, v2: int) -> int:
        if v1 == v2:
            return 0

        if v1 < v2:
            return -1

        if v1 > v2:
            return 1

    def add(self, value):
        new_node = Node(value)
        node = self.head
        prev = node.prev

        if node is None:  # if the list is empty
            self.head = new_node
            self.tail = new_node
            return

        while node is not None:
            comp_result = self.compare(value, node.value)
            if (self.__ascending and comp_result <= 0) or (not self.__ascending and comp_result >= 0):
                if prev is None:  # insert in the head
                    new_node.next = node
                    node.prev = new_node
                    self.head = new_node
                else:  # insert in the middle
                    new_node.prev = prev
                    new_node.next = node
                    prev.next = new_node
                    node.prev = new_node
                break
                prev = node
                node = node.next
            if node is None:  # insert in the end
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        return

    def find(self, val):
        node = self.head
        while node is not None:
            comp_result = self.compare(val, node.value)
            if (self.__ascending and comp_result > 0) or (not self.__ascending and comp_result < 0):
                break
            if comp_result == 0:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            comp_result = self.compare(val, node.value)
            if (self.__ascending and comp_result > 0) or (not self.__ascending and comp_result < 0):
                break
            if comp_result == 0 and node.prev is None and node.next is None:  # if node is head and that's the only item
                self.head = None
                self.tail = None
            if comp_result == 0 and node.prev is None and node.next is not None:  # if node is head and more than 1 item
                self.head = node.next
                self.head.prev = None
            if comp_result == 0 and node.next is None:  # if node is tail
                self.tail = node.prev
                self.tail.next = None
            if comp_result == 0 and node.next is not None:  # if node is in the middle
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next
        return None

    def clean(self, asc: bool):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self) -> int:
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self) -> list:
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc: bool):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str):
        v1, v2 = v1.strip(), v2.strip()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

