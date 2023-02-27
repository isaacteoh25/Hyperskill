def rec_sum(n):
    # write the insides here!
    if n <= 1:
        return n
    return rec_sum(n-1) + n

print(rec_sum(9))