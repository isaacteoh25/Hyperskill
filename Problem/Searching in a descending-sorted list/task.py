def binary_search(elements, target):
    index = -1
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        # if elements[middle] == target:
        if target >= elements[middle]:
            if elements[middle] == target:
                index = middle
            right = middle - 1
        else:
            left = middle + 1

    return index

# elements = [int(x) for x in input().split()]
# target = int(input())
elements = [int(x) for x in "5 5 4 4 4 4 3 2 1".split()]
target = 4

result = binary_search(elements, target)
# if result == len(elements):
#     result = -1
print(result)
import bisect
L = [-int(x) for x in input().split()]
t = -int(input())

n = bisect.bisect_left(L, t)

if n not in range(len(L)):
    print(-1)
elif L[n] == t:
    print(n)
else:
    print(-1)