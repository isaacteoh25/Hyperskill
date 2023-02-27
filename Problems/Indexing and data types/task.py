import numpy as np

array = np.array([[0, 2, 1998],
                  [12, 0, 1212],
                  [21, 0, 0],
                  [7, 0, 2019]])
n = int(input())
print(np.bool_(array[n]))
# for a in array[0]:
#     print(np.bool(a))