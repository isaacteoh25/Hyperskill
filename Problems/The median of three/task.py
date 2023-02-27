def partition(lst, start, end):
    three = [(lst[start], start),
             (lst[(start + end) // 2], (start + end) // 2),
             (lst[end], end)]
    three.sort()
    lst[start], lst[three[1][1]] = lst[three[1][1]], lst[start]
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return three[1][1]


def choose_median(lst, start, end):
    mid = (start + end) // 2
    median = 0
    if lst[start] > lst[mid] > lst[end] or lst[start] < lst[mid] < lst[end]:
        median = mid
    if lst[start] > lst[end] > lst[mid] or lst[start] < lst[end] < lst[mid]:
        median = end
    if lst[end] > lst[start] > lst[mid] or lst[end] < lst[start] < lst[mid]:
        median = start

    return median


def partition(lst, start, end):
    pivot = choose_median(lst, start, end)
    lst[start], lst[pivot] = lst[pivot], lst[start]

    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]

    return pivot


lst = [int(x) for x in input().split()]
print(partition(lst, 0, len(lst) - 1))
print(*lst)

input_list = list(map(int, input().split()))
print(partition(input_list, 0, len(input_list) - 1))
print(*input_list)