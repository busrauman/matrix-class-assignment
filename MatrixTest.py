from Matix import *
from MatrixUtils import *

A = Matrix(2,2)
B = Matrix(2,2)
B.setMatrix()
A.setMatrix()
A.setItem(0,0,5)
A.setItem(0,1,6)
A.showMatrix()
B.showMatrix()
trace(A.rows)
#print(A.matrixMultiplication(B.rows))
print(matrixMultiplication(A.rows,B.rows))

print("trace : %d" % trace(A.rows))
print(determinant(A.rows))

print(scalarMultiplication(A.rows,3))
