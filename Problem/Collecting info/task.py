import numpy as np

def collect_info(array):
    return 'Shape: '+str(array.shape) + "; dimensions: "+ str(array.ndim)+"; length: " +str(len(array))+"; size: "+ str(array.size)+''

# a =collect_info(np.array([[[1, 1, 1], [2, 2, 2]],
#                    [[3, 3, 3], [4, 4, 4]]]))
# print(a)
# "Shape: (2, 2, 3); dimensions: 3; length: 2; size: 12".
# "Shape: (2, 2, 3); dimensions: 3; length: 2; size: 12"
array = np.linspace(20, 42, num=11)
print(array[4])