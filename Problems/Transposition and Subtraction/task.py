import numpy as np
# a1 = np.array([[10, 9], [8, 7]])
# a2 = np.array([6, 5])
a1 = np.array([[int(input()), int(input())], [int(input()), int(input())]])
a2 = np.array([int(input()), int(input())])
a3 = np.transpose(a1)
a4 = np.subtract(a3, a2)
print(a4)