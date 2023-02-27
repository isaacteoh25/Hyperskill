def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


count = 0


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    global count
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    count += 1
    return merge(left, right)


merge_sort([int(el) for el in input().split()])
print(count)