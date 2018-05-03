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

    def setItem(self, i, j, item):
        if self.m >= i and self.n >=j:
            self.rows[i][j] = item

    def scalarMultiplication(self,multiplier):
        for i in range(self.m):
            for j in range(self.n):
                self.rows[i][j] *= multiplier

    def trace(self):
        trace = 0
        if self.m == self.n:
            for k in range(self.m):
                trace += self.rows[k][k]
        return trace

    def transpoze(self):
        transpoze=[[0] * self.n for x in range(self.m)]

        if self.m == self.n:
            for i in range(self.m):
                for j in range(self.n):
                    transpoze[j][i] = self.rows[i][j]
        return transpoze

    def matrixMultiplication(self,matrix):
        result = [[0] * self.n for x in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.n):
                    result[i][j] += self.rows[i][k] * matrix[k][j]
        return result


#matrise liste gönder ve set et
    def determinant(self):
        determinant = 0

        if self.m != self.n:
            print("Determinant hesabı için satır ve sütün sayıları aynı olan bir matris girmelisiniz")
        else:
            if self.m == 1 and self.n == 1:
                determinant =  self.rows[0][0]
            elif self.m == 2 and self.n == 2:
                determinant = (self.rows[0][0] * self.rows[1][1]) - (self.rows[0][1] * self.rows[1][0])
            else:
                # silme işlemi
                return determinant

        return determinant

    def removeRowAndCol(self,i,j):
        newMatrix=[[0] * (self.n-1) for x in range(self.m-1)]
        row=0
        col=0
        for x in range(self.m):
            if x != i:
                for y in range(self.n):
                    if x != i and y != j:
                        newMatrix[row][col] = self.rows[x][y]
                        col += 1

            if col >= (self.n - 1):
                 row +=1
            col = 0
        return newMatrix