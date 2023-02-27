def search(numbers, target, a, b):
    # index = -1
    # for i in range(int(a), int(b)):
    #     if int(numbers[i]) == target:
    #         index = i
    #         break
    #
    # return index
    for i, elem in enumerate(numbers[a:b], a):
        if elem == target:
            return i
    return -1


nums = tuple(map(int, input().split()))
target = int(input())
a, b = input().split()
# b = int(input())
# nums = "5 3 1 2 4".split()
# target = 1
# a, b = "1 4".split()
print(search(nums, target, a, b))