def InsertionSortStep(array: list, step: int, i: int):
    for j in range(i, len(array), step):
        current_value = array[j]
        position = j

        while position >= step and array[position - step] > current_value:
            array[position] = array[position - step]
            position -= step

        array[position] = current_value
