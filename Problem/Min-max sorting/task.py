
# def selection_sort_minmax(elements):
#     for i in range( 0, len(elements)-(len(elements)%2), 2):
#         min_i = i
#         max_i = i + 1
#         if elements[min_i] > elements[max_i]:
#             elements[min_i], elements[max_i] = elements[max_i], elements[min_i]
#         for j in range(i, len(elements)):
#             if elements[j] < elements[min_i]:
#                 min_i = j
#             if elements[j] > elements[max_i]:
#                 max_i = j
#         elements[i], elements[min_i], elements[i+1], elements[max_i] = elements[min_i], elements[i], elements[max_i], elements[i+1]
#     return elements
#
# def printArray(a, n):
#     for i in range(n):
#         print(a[i], end = " ")
# b = [int(x) for x in input().split()]
# # "3 8 1 2 5 8".split()
# a = selection_sort_minmax(b)
# n = len(a)
# printArray(a, n)

arr = [int(x) for x in input().split()]
i = 0

while i < len(arr):
    if i % 2 == 0:
        index = arr[i:].index(min(arr[i:]))
    else:
        index = arr[i:].index(max(arr[i:]))

    arr[i], arr[i + index] = arr[i + index], arr[i]

    i += 1

print(' '.join(str(el) for el in arr))

import itertools
k = list(map(int, input().split()))
print(*list(itertools.chain(*list(zip(sorted(k), sorted(k, reverse=True)))))[:len(k)])