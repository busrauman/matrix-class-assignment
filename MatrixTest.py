from Matix import *


A = Matrix(3,3)
A.setMatrix()
A.setItem(0,0,5)
A.setItem(0,1,6)
A.showMatrix()
print(A.determinant(A.rows))