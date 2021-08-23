matriza = [[0, 3], [2, -5]]
matrizb = [[-2, 4], [0, -1]]
matrizc = [[4, 2], [-6, 0]]
matrizresult = [[0, 0], [0, 0]]

print('=-=' *10)
print('Calcule as matrizes A+B-4*C')
print('=-=' *10)

A = [[0, 3], [2, -5]]
print('\nMatriz A:')
for i in range(0, 2):
    for j in range(0, 2):
        print('[{:^5}]'.format(A[i][j]), end='')
    print()

B = [[-2, 4], [0, -1]]
print('\nMatriz B:')
for i in range(0, 2):
    for j in range(0, 2):
        print('[{:^5}]'.format(B[i][j]), end='')
    print()

C = [[4, 2], [-6, 0]]
print('\nMatriz C:')
for i in range(0, 2):
    for j in range(0, 2):
        print('[{:^5}]'.format(C[i][j]), end='')
    print()

print('\nResultado:')
for linha in range(0, 2):
    for coluna in range(0, 2):
        matrizresult[linha][coluna] = matriza[linha][coluna] + matrizb[linha][coluna] - (matrizc[linha][coluna] * 4)

print('-' * 15)
for linha in range(0, 2):
    for coluna in range(0, 2):
        print('[{:^5}]'.format(matrizresult[linha][coluna]), end='')
    print()
print('-' * 15)
