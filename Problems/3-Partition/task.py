import time

def sort1(A, l, r):

    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l  # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]  # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
    # in the quick_sort function.
    while i <= gt:  # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


start_time = time.time()
a = list(map(int, input().split()))

e1, e2 = sort1(a, 0, len(a) - 1)

print("--- %s seconds ---" % (time.time() - start_time))
print(e1, e2)
print(*a)


def partition(lst, start, end):
    j = start
    for i in range(start + 1, end + 1):
        if lst[i] < lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    print(j, end=" ")
    for i in range(j + 1, end + 1):
        if lst[j] == lst[i]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    print(j)


list_ = [int(x) for x in input().split()]
partition(list_, 0, len(list_) - 1)
print(*list_)