from linked_list import Node, LinkedList
import random


def compare_and_sum(first_l_list, second_l_list):
    if first_l_list.len() != second_l_list.len():
        return None
    first_node = first_l_list.head
    second_node = second_l_list.head

    result_list = LinkedList()

    while first_node is not None and second_node is not None:
        sum_value = first_node.value + second_node.value
        result_list.add_in_tail(Node(sum_value))
        first_node = first_node.next
        second_node = second_node.next

    return result_list


if __name__ == '__main__':
    length = 20
    first_test_arr = random.sample(range(-1000, 1000), 20)
    second_test_arr = random.sample(range(-1000, 1000), 20)

    first_l_list, second_l_list = LinkedList(), LinkedList()

    for i in range(length):
        first_l_list.add_in_tail(Node(first_test_arr[i]))
        second_l_list.add_in_tail(Node(second_test_arr[i]))
    print(first_test_arr)
    print(second_test_arr)
    compare_and_sum(first_l_list, second_l_list).print_all_nodes()
