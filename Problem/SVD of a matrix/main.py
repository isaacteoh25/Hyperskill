import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([[a, b], [c, d]])
svd_matr = np.linalg.svd(arr)
print(svd_matr)