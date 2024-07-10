def KnuthSequence(array_size: int) -> list[int]:
    seq = []
    h = 1
    while h < array_size or not seq:
        seq.insert(0, h)
        h = 3 * h + 1
    return seq
