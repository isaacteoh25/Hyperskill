# l1 = "3 1 2 5 4".split()
# l2 = "1 2 3 4 5".split()
l1 = tuple(map(int, input().split()))
l2 = tuple(map(int, input().split()))
res = []


def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2;
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1
        # If we reach here, then the element
        # was not present
    return -1

for i in l1:
    res.append(binary_search(l2, 0, len(l2)-1, i))
print(*res)

# nlist = tuple(map(int, input().split()))
# olist = tuple(map(int, input().split()))

# for i in nlist:
#     print(bfind(olist, i), end=' ')