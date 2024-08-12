def MergeSort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = MergeSort(array[:mid])
    right_half = MergeSort(array[mid:])

    sorted_array = []

    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1

    while i < len(left_half):
        sorted_array.append(left_half[i])
        i += 1

    while j < len(right_half):
        sorted_array.append(right_half[j])
        j += 1

    return sorted_array
