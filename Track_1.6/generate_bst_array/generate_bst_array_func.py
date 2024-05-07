from typing import Optional


def buildBBST(array: list, sorted_bst_array: list, index: int) -> Optional[list]:
    # Function for recursive creating bst array
    if not array:
        return

    # middle item index in array
    array_length = len(array)
    middle_item_index = array_length // 2
    # Middle item put in the root
    sorted_bst_array[index] = array[middle_item_index]

    # Recursive call for left and right sides

    # For left side index will be  2*index + 1
    buildBBST(array[:middle_item_index], sorted_bst_array, 2 * index + 1)
    # For right side index will be  2*index + 2
    buildBBST(array[middle_item_index + 1:], sorted_bst_array, 2 * index + 2)


def GenerateBBSTArray(a: list[int]) -> list:
    sorted_bst_array = [None] * len(a)

    a.sort()

    # filling result array
    buildBBST(a, sorted_bst_array, 0)

    return sorted_bst_array

