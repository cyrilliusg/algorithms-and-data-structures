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

    def add(self, value: int):
        new_node = Node(value)
        node = self.head

        if self.head is None:  # if the list is empty
            self.head = new_node
            self.tail = new_node
            return

        while node is not None:
            comp_result = self.compare(value, node.value)
            if (self.__ascending and comp_result <= 0) or (not self.__ascending and comp_result >= 0):
                if node == self.head:  # insert in the head
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    break
                # insert in the middle
                new_node.prev = node.prev
                new_node.next = node
                node.prev.next = new_node
                node.prev = new_node
                break

            node = node.next

            if node is None and \
                    ((self.__ascending and comp_result == 1) or
                     (not self.__ascending and comp_result == -1)
                    ):  # if value is the biggest in the list
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

    def find(self, val: int):
        node = self.head
        while node is not None:
            comp_result = self.compare(val, node.value)
            if (self.__ascending and comp_result < 0) or (not self.__ascending and comp_result > 0):
                break
            if comp_result == 0:
                return node
            node = node.next
        return None

    def delete(self, val: int):
        if self.head is None:
            return

        node = self.head

        while node is not None:
            comp_result = self.compare(val, node.value)
            if (self.__ascending and comp_result < 0) or (not self.__ascending and comp_result > 0):
                break

            if comp_result == 0:
                if node == self.head:  # if the value is the first
                    self.head = node.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None  # The list went blank
                elif node == self.tail:  # if the last one
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.prev.next, node.next.prev = node.next, node.prev

            node = node.next

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
