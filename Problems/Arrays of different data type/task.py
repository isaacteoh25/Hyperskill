import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)
i = int(input())
f = int(input())
# print(np.str_(array[i]))
print(array[i].astype(np.str_))
# print(np.arange(array[i], dtype=np.int64))
print(np.float64(array[f]))