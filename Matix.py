class Matrix:
    def __init__(self,m,n,init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []

        self.m = m
        self.n = n

    def showMatrix(self):
        print(self.rows)

    def getItem(self,i,j):
        if self.m >= i  and self.n >= j:
            return self.rows[i][j]

    def changeItem(self,i,j,item):
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
        return self.rows

