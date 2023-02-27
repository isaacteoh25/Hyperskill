import numpy as np

# array = np.array([[212, 215, 434, 2, 0],
#                   [6, 447, 0, 4, 143],
#                   [10, 478, 601, 602, 3]], dtype=np.float64)
# print(array[2])
# row = int(input())
# step = int(input())
# print(array[row,::step].astype(np.int8))

array = np.array([[[14, 5], [8, 0]], [[13, 7], [18, 5]]])
print(array.sum(axis=2))