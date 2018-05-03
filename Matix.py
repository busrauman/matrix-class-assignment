class Matrix:
    def __init__(self,m,n,init=True):
        if init:
            self.rows = [[0] * n  for x in range(m)]
        else:
            self.rows = []

        self.m = m
        self.n = n

    def setMatrix(self):
        k=1
        for x in range(self.m):
            for y in range(self.n):
                self.rows[x][y] = k
                k += 1

    def showMatrix(self):
        print(self.rows)

    def getItem(self,i,j):
        if self.m >= i  and self.n >= j:
            return self.rows[i][j]
        else:
            print("Olmayan bir indis değerine ulaşmaya çalıştınız tekrar deneyiniz")

    def setItem(self, i, j, item):
        if self.m >= i and self.n >=j:
            self.rows[i][j] = item
        else:
            print("Olmayan bir indis değerine ulaşmaya çalıştınız tekrar deneyiniz")


    def scalarMultiplication(self,multiplier):
        for i in range(self.m):
            for j in range(self.n):
                self.rows[i][j] *= multiplier

    def trace(self):
        trace = 0
        if self.m == self.n:
            for k in range(self.m):
                trace += self.rows[k][k]
        else:
            print("Lütfen bir kare matris giriniz")
        return trace

    def transpoze(self):
        transpoze=[[0] * self.n for x in range(self.m)]
        if self.m == self.n:
            for i in range(self.m):
                for j in range(self.n):
                    transpoze[j][i] = self.rows[i][j]
        else:
            print("Lütfen kare bir matris giriniz")
        return transpoze

    def matrixMultiplication(self,matrix):
        result = [[0] * self.n for x in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.n):
                    result[i][j] += self.rows[i][k] * matrix[k][j]
        return result


    def determinant(self, matrix):
        determinant = 0
        if len(matrix) == 2:
             return  (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        for i in range(len(matrix)):
            pow = ((-1)**i)
            item = matrix[0][i]
            m = self.removeRowAndCol(0,i,matrix)

            determinant += pow * item * self.determinant(m)
            print("pow * item * matris = %d * %d : " % (pow,item))
            print(matrix)
            print("determinant : %d" % determinant)
        return determinant

    def removeRowAndCol(self,i,j,matrix):
        newMatrix=[[0] * (len(matrix)-1) for x in range(len(matrix[0])-1)]
        row=0
        col=0
        for x in range(len(matrix)):
            if x != i:
                for y in range(len(matrix[0])):
                    if x != i and y != j:
                        newMatrix[row][col] = matrix[x][y]
                        col += 1
            if col >= (self.n - 1):
                 row +=1
            col = 0
        return newMatrix