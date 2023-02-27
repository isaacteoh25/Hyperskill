# def search(numbers, target):
#     try:
#     # for i, elem in enumerate(numbers):
#     #     if int(elem) == target:
#     #         index = i
#     #         break
#         res = max(idx for idx, val in enumerate(numbers)
#                   if val == target)
#         return res
#     except:
#         res = -1
#         return res
# backward
# def search(numbers, target):
#     index = -1
#     numbers = numbers.split()
#     if len(numbers) > 1:
#         counter = len(numbers) - 1
#     elif int(numbers[0]) == target:
#         return 0
#     else:
#         return index
#
#     for i in range(counter, 0, -1):
#         if int(numbers[i]) == target:
#             index = counter
#
#             break
#         counter -= 1
#
#     return index
# numbers = input()
# numbers ="3 5 9 11 9"
# target = "9"
# target = input()
# print(search(numbers.split(" "), target))
def search(numbers, target):
    indices = tuple(i for i, num in enumerate(numbers) if num == target)
    return max(indices) if indices else -1

nums = tuple(map(int, input().split()))
print(search(nums, int(input())))