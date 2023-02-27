def kth(numbers, target, k):
    # indices = tuple(i for i, num in enumerate(numbers) if num == target)
    # if len(indices) < k:
    #     return -1
    # else:
    #     return indices[k-1]
    k_count = 0

    for i, elem in enumerate(numbers):
        if elem == target:
            k_count += 1
            if k_count == k:
                return i
    return -1


nums = tuple(map(int, input().split()))
# nums = tuple(map(int, "7 6 3 1 2 2 3 4".split()))
# k = 1
print(kth(nums, int(input()), int(input())))