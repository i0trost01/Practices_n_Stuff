def distance(strand_a, strand_b):
    if len(strand_a)==len(strand_b):
        union=[i for i, j in zip(strand_a, strand_b) if i == j]
        return len(strand_a)-len(union)
    else:
        raise ValueError("strand a and strand b do not have the same length")



