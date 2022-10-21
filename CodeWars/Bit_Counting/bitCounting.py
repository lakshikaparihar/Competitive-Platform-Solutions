def count_bits(n):
    bin_rep = bin(n)
    return bin_rep.count("1")