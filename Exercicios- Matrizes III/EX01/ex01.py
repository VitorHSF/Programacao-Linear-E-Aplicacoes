matriz_a  = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
matriz_b  = [[1, 1, 1], [0, 2, 3], [5, 5, 1]]
matriz_c  = [[1, -2, -3], [0, -4, 4], [0, 0, 0]]
matrizai  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizbi  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizci  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



print('Matriz A:')
print()
for coluna in matriz_a:
    print(coluna)
print()


print('Matriz B:')
print()
for coluna in matriz_b:
    print(coluna)
print()

print('Matriz C:')
print()
for coluna in matriz_c:
    print(coluna)
print()


def determinant(matrix, mul):

    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer

matrizc = [[1, -2, -3], [0, -4, 4], [0, 0, 0]]



deta = determinant(matriz_a, 1)
detb = determinant(matriz_b, 1)
detc = determinant(matriz_c, 1)
print('Determinante A  =',deta)


if(deta==0):
    print('Matriz Inversa de A Não Existe, Determinante =',deta)
else:

    def inv2(matriza):
        d = deta
        return [[matriza[0][0] / -d, matriza[0][1] / -d, matriza[0][2] / -d],
                [matriza[1][0] / -d,matriza[1][1] / -d, -matriza[1][2] / -d],
                [matriza[2][0] / -d, matriza[2][1] / -d, matriza[2][2] / -d]]

    matrizai = inv2(matriz_a)

    print()
    print('Matriz Inversa de A')
    print('=-' * 8)
    for l in range(3):
        for c in range(3):
            print(f'[{matrizai[l][c]:^5}]', end='')
        print()
    print('=-' * 8)


if(detb==0):
    print('Matriz Inversa de B Não Existe, Determinante =',detb)
else:

    def calculating_inverse_matrix():
        matrix1 = [
            [1, 1, 1],
            [0, 2, 3],
            [5, 5, 1]
        ]
        inv = inverse(matrix1)
        print("Matriz Inversa de B:")
        print('=-' * 12)
        for row in inv:
            print("", row)


    def inverse(matrix1):

        if not issquare(matrix1):
            return ZeroDivisionError
        numRows = len(matrix1)
        invMatrix = give_identity_mat(numRows)

        for i in range(numRows):
            if matrix1[i][i] == 0:
                return ZeroDivisionError

            if matrix1[i][i] != 1:
                factor = matrix1[i][i]
                divide(matrix1, i, factor)
                divide(invMatrix, i, factor)

            for j in range(numRows):
                if i != j:
                    if matrix1[j][i] != 0:
                        factor = matrix1[j][i]
                        rowsub(matrix1, i, j, factor)
                        rowsub(invMatrix, i, j, factor)

        return invMatrix


    def give_identity_mat(num_rows):
        identitymat = [[0 for i in range(num_rows)] for i in range(num_rows)]
        for i in range(0, num_rows):
            identitymat[i][i] = 1
        return identitymat


    def rowsub(matrix, row1, row2, factor):
        for i in range(len(matrix[row2])):
            matrix[row2][i] -= factor * matrix[row1][i]


    def issquare(M):
        return len(M[0]) == len(M)


    def multiply(matrix, row, factor):
        for i in range(len(matrix[row])):
            matrix[row][i] *= factor


    def divide(matrix, row, factor):
        for i in range(len(matrix[row])):
            matrix[row][i] /= factor

    print()
    print('Determinante de B  =', detb)
    print()
    calculating_inverse_matrix()
    print('=-' * 12)

#Parte do C

if(detc==0):
    print()
    print('Matriz Inversa de C Não Existe, Determinante =',detc)

else:
    def det2(matrizc):
        return matrizc[0][0] * matrizc[1][1] - matrizc[0][1] * matrizc[1][0]


    def inv2(matrizc):
        d = det2(matrizc)
        return [[matrizc[1][1] / d, -matrizc[0][1] / d], [-matrizc[1][0] / d, matrizc[0][0] / d]]


    matrizci = inv2(matrizc)

    print()
    print('Determinante C  =', detc)
    print('Matriz Inversa de C')
    print('=-' * 8)
    for l in range(3):
        for c in range(3):
            print(f'[{matrizci[l][c]:^5.2f}]', end='')
        print()
    print('=-' * 8)