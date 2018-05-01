from Matix import *


A = Matrix(3,3)
A.changeItem(0,0,1)
A.changeItem(1,1,2)
A.changeItem(2,2,3)

A.showMatrix()

#A.scalarMultiplication(2)

A.showMatrix()

print(A.trace())