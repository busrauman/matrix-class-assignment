def trace(arg0):
    trace = 0
    if len(arg0) == len(arg0[0]):
        for k in range(len(arg0)):
            trace += arg0[k][k]
    else:
        print("Lütfen bir kare matris giriniz")
    return trace


def transpoze(arg0):
    transpoze = [[0] * self.n for x in range(self.m)]
    if len(arg0) == len(arg0[0]):
        for i in range(len(arg0)):
            for j in range(len(arg0[0])):
                transpoze[j][i] = arg0[i][j]
    else:
        print("Lütfen kare bir matris giriniz")
    return transpoze


#eşit boyuttaki matrisler için çalışıyor düzenle burayı
def matrixMultiplication(arg0, arg1):
    result = [[0] * len(arg0) for x in range(len(arg1[0]))]
    if len(arg0[0]) != len(arg1):
        print("Birinci matrisin satır sayısı  ile ikinci matrisin sütün sayısı eşit olmalıdır ")
    else:
        for i in range(len(arg0)):
            for j in range(len(arg1[0])):
                for k in range(len(arg0[0])):
                    result[i][j] += arg0[i][k] * arg1[k][j]
    return result


def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        determinant = 0
        if len(matrix) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        for i in range(len(matrix)):
            pow = ((-1) ** i)
            item = matrix[0][i]
            m = coFactor(0, i, matrix)
            determinant += pow * item * determinant(m)
        return determinant
    else:
        print("Lütfen kare matris giriniz")


def coFactor(i, j, matrix):
    newMatrix = [[0] * (len(matrix) - 1) for x in range(len(matrix[0]) - 1)]
    row = 0
    col = 0
    for x in range(len(matrix)):
        if x != i:
            for y in range(len(matrix[0])):
                if x != i and y != j:
                    newMatrix[row][col] = matrix[x][y]
                    col += 1
        if col >= (len(matrix[0]) - 1):
            row += 1
        col = 0
    return newMatrix


def scalarMultiplication(matrix,multiplier):
     for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= multiplier

     return matrix


def showMatrix(matrix):
    print(matrix)

def setIdentityMatrix(size):
    matrix = [[0] * size for x in range(size)]
    for k in range(size):
        matrix[k][k] = 1
    return  matrix

def inverseMatrixWithGussianElimination(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row - 1):
        if matrix[i][i] == 0:
            for j in range(i+1,row):
                if(matrix[j][i] == 0):
                    if((j+1) == row ):
                        print("Matrisin tersi hesaplanamaz.")
                else:
                    # row i row j ile swap edilir
                    matrix = swapRows(matrix, i, j)



        for k in range(i+1,row):
            r = matrix[k][i] / matrix[i][i]
            # i. satırı r ile çarp k. satırdan çıkar
            matrix = elemination(matrix,i,k,r)
    return matrix


def elemination(matrix,i,k,r):
    for x in range(len(matrix)):
        matrix[i][x] *= r
        matrix[i][x] = matrix[i][k] - matrix[i][x]
    return matrix


def swapRows(matrix,i,k):
    for x in range(len(matrix)):
        tmp = matrix[i][x]
        matrix[i][x] = matrix[k][x]
        matrix[k][x] =tmp
    return matrix






