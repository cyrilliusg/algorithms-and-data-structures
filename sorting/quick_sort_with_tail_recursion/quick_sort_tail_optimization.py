def ArrayChunk(M: list[int], left: int, right: int) -> int:
    if not M:
        return 0

    while True:
        N_index = (left + right) // 2
        N = M[N_index]

        i1 = left
        i2 = right

        while True:
            while M[i1] < N:
                i1 += 1

            while M[i2] > N:
                i2 -= 1

            if i1 == i2 - 1 and M[i1] > M[i2]:
                M[i1], M[i2] = M[i2], M[i1]
                break

            if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
                return N_index

            M[i1], M[i2] = M[i2], M[i1]

            if i1 == N_index:
                N_index = i2
            elif i2 == N_index:
                N_index = i1


def QuickSortTailOptimization(arr, low, high):
    while low < high:
        q = ArrayChunk(arr, low, high)

        QuickSortTailOptimization(arr, low, q - 1)

        low = q + 1
