def merge(left, right):

    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
    return merged



# print(merge(list(map(int, "10 8 5 4 3 2".split())), list(map(int, "9 7 6 1".split()))))