import numpy as np

a1 = np.array([[int(input()), int(input())], [int(input()), int(input())]])
a2 = np.array([int(input()), int(input())])
a3 = np.matmul(a1, a2)
print(a3)