import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

a1 = np.array([a, b, c, d])
spec = np.where(a1 >= 45)
print(a1[spec])