# import np as np
import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([[a, b], [c, d]])
rank = np.linalg.matrix_rank(arr)
print(rank)  # 2