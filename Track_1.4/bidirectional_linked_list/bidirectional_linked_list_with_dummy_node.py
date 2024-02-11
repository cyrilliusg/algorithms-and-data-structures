from bidirectional_linked_list import Node, LinkedList2


class Dummy(LinkedList2):
    def __init__(self):
        super().__init__(head=Node(None), tail=Node(None))  # dummy head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev  # actual tail node
        item.next = self.tail  # dummy node
        self.tail.prev.next = item  # from penultimate to tail
        self.tail.prev = item  # new actual tail node

    def delete(self, value, all=False):
        current_node = self.head.next
        while current_node.value is not None:
            if current_node.value == value:
                current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
                if not all:
                    break
            current_node = current_node.next


if __name__ == '__main__':
    l = Dummy()
    l.add_in_tail(Node(1))
    l.add_in_tail(Node(2))
    l.add_in_tail(Node(1))
    l.delete(1, all=False)
    l.print_all_nodes()
