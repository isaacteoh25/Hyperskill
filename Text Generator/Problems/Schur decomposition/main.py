import scipy
from scipy.linalg import schur, eigvals
import numpy

A = numpy.array([[0, 2, 2], [2, 1, 2], [1, 0, 1]])

# your code here
Z,T = schur(A)

print(numpy.trace(Z) + numpy.trace(T))
