#implement the binary search here
import math

frames = [0, 3, 5, 8, 9, 12, 22, 156, 9009, 75327, 4835160]
def bin_search(frames_list, target, left=0, right=None):
    if right is None:
        right = len(frames_list) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if frames_list[middle] == target:
        return middle
    if frames_list[middle] < target:
        return bin_search(frames_list, target, middle + 1, right)
    return bin_search(frames_list, target, left, middle - 1)


n, w, h = list(map(int, input().split()))
length = math.ceil(math.sqrt(n * (w * h)))
result = -1
while result == -1:
    result = bin_search(frames, length)
    length += 1
print(result)