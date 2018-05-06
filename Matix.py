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



