from Matix import *


A = Matrix(3,3)
A.changeItem(0,0,1)
A.changeItem(1,1,2)
A.changeItem(2,2,3)
A.changeItem(0,1,5)
A.changeItem(0,2,4)
A.changeItem(1,0,6)
A.changeItem(2,0,7)

B = Matrix(3,3)
B.changeItem(0,0,1)
B.changeItem(1,1,2)
B.changeItem(2,2,3)
B.changeItem(0,1,5)
B.changeItem(0,2,4)
B.changeItem(1,0,6)
B.changeItem(2,0,7)

#A.scalarMultiplication(2)
#print(A.transpoze())

A.showMatrix()
B.showMatrix()

print(A.matrixMultiplication(B.rows))

