from math import ceil
array= []
# def method(array, left, right, value):
#     if left >= right:
#         return 0
#     elif left == right-1:
#         return 1 if array[left] == value else 0
#     else:
#         middle = (left + right) // 2
#         return method(array, left, ceil(middle), value) \
#                + method(array, ceil(middle), right, value)
def method(array, left, right):
    if left == right:
        if array[left] % 2 == 0:
            return 1
        else:
            return 0
    else:
        middle = (left + right) // 2
        return method(array, left, middle)\
               + method(array, middle + 1, right)
# print(method([2, 3, 3, 3, 5, 2], 0, 4))
# print(method([1, 2, 3, 3, 3], 0, 4, 3))
# print(method([2, 2, 2, 2, 2], 0, 4, 2))
# print(method([1, 2, 3, 5, 5], 0, 5, 5))
# print(method([1, 2, 3, 4, 5], 0, 4, 5))
# print(method([1, 1, 1, 2, 2], 1, 3, 1))
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


# arr = [10, 7, 8, 9, 1, 5]
arr = [12, 3, 7, 55, 27, 18, 44, 2]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

