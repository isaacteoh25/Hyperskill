import numpy
from numpy.linalg import inv

A = numpy.array([[1, 2], [2, 3]])

# your code
print(numpy.trace(inv(A)))
