from Matix import *
from MatrixUtils import *

A = Matrix(3,3)
B = Matrix(3,2)
B.setMatrix()
A.setMatrix()
#A.setItem(0,1,0)
A.setItem(1,1,0)


#print(A.matrixMultiplication(B.rows
print(A.rows)
print(inverseMatrixWithGussianElimination(A.rows))

