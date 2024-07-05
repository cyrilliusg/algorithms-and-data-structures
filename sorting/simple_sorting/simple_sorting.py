def SelectionSortStep(array: list, i: int):
    min_idx = i

    for j in range(i + 1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j

    if min_idx != i:
        array[i], array[min_idx] = array[min_idx], array[i]


def BubbleSortStep(array: list) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            return False
    return True
