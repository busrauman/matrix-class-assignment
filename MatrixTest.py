from Matix import *


A = Matrix(5,5)
A.setMatrix()

#A.scalarMultiplication(2)
#print(A.transpoze())

A.showMatrix()

X=A.removeRowAndCol(1,3)
print(X)