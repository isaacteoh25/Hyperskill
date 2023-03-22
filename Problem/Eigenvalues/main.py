import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([[a, b], [c, d]])
w, v = np.linalg.eig(arr)

# print(np.linalg.eig(arr))
# (array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356],
#        [ 0.56576746, -0.90937671]]))

print(w)
# [-0.37228132  5.37228132]

# print(v)