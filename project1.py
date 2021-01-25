# import sympy
from sympy import *

M = Matrix([[1, 0, 1], [2, 3, 4], [-1, -3, -3]])
print("Matrix : {} ".format(M))

# Use sympy.rref() method
M_rref = M.rref()

print("The Row echelon form of matrix M and the pivot columns : {}")
print(M_rref)