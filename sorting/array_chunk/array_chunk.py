def ArrayChunk(M):
    if not M:
        return 0

    while True:
        N_index = len(M) // 2
        N = M[N_index]

        i1 = 0
        i2 = len(M) - 1
        while M[i1] < N:
            i1 += 1

        while M[i2] > N:
            i2 -= 1

        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            continue

        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return N_index

        M[i1], M[i2] = M[i2], M[i1]

        if i1 == N_index:
            N_index = i2
        elif i2 == N_index:
            N_index = i1

        i1 += 1
        i2 -= 1
