
# vals = [int(el) for el in input().split()]
# vals.sort(reverse=True)
# for val in vals:
#     print(val, end=" ")

def partition(lst, start, end):
    three = [lst[start], lst[(start + end) // 2], lst[end]]
    three.sort()
    pivot = three[1]
    greater = []
    equal = []
    smaller = []

    for elem in lst[start:(end + 1)]:
        if elem > pivot:
            greater.append(elem)
        elif elem < pivot:
            smaller.append(elem)
        else:
            equal.append(elem)

    lst[start:(end + 1)] = greater + equal + smaller
    if greater:
        greater_end = start + len(greater) - 1
    else:
        greater_end = None
    if smaller:
        smaller_start = end - len(smaller) + 1
    else:
        smaller_start = None
    return greater_end, smaller_start


def quick_sort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start >= end:
        return

    greater_end, smaller_start = partition(lst, start, end)
    if greater_end is not None:
        quick_sort(lst, start, greater_end)
    if smaller_start is not None:
        quick_sort(lst, smaller_start, end)


dates = list(map(int, input().split()))
quick_sort(dates)
print(*dates)
