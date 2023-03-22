import numpy as np

a = int(input())
b = int(input())
c = int(input())
# a1 = np.array([19, 92, 53])
a1 = np.array([a, b, c])
spec = np.where(a1 > 15)

if len(a1[spec]) == 3:
    print(True)
else:
    print(False)