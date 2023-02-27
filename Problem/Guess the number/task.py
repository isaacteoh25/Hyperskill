x = int(input())
lx, rx = (int(n) for n in input().split())
tries = 0

# elements =[]
# for a in range (lx, rx+1):
#     elements.append(a)
elements = [num for num in range(lx, rx + 1)]
# put your code here
# def binary_search(elements, x):
#     global tries
#
#     lx, rx = 0, len(elements) - 1

# while lx <= rx:
#     middle = (lx + rx) // 2
#     if elements[middle - 1] == x:
#         tries += 1
#         break
#     elif x < elements[middle - 1]:
#         rx = middle - 1
#         tries += 1
#     else:
#         lx = middle + 1
#         tries += 1

    # return -1
while True:
    tries += 1
    mid = (rx + lx) // 2
    if mid == x:
        break
    if mid > x:
        rx = mid - 1
    else:
        lx = mid + 1

# elements = [3, 4, 6, 7, 9, 12, 15, 20, 25]
# target = 5
# tries = binary_search(elements, x)

print(tries)