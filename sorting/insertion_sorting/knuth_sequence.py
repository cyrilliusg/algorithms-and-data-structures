def KnuthSequence(array_size: int) -> list[int]:
    # Generate the Knuth sequence dynamically
    seq = []
    h = 1
    while h < array_size:
        seq.insert(0, h)  # Prepend to the sequence for descending order
        h = 3 * h + 1
    return seq
