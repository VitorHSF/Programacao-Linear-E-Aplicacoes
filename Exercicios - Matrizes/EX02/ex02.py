matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 4):
        if linha == coluna:
            matriz[linha][coluna] = ((linha + 1) + (coluna + 1))
        else:
            matriz[linha][coluna] = ((2 * linha) + 1) - ((2 * coluna) + 1)

a = int(matriz[1][1])
b = int(matriz[2][3])

print('=-' * 15)

for linha in range(0, 3):
    for coluna in range(0, 4):
        print('[{:^3}]'.format(matriz[linha][coluna]), end='')
    print()

print('\nA soma do valor de a22 e a34 é {}'.format(a+b))
