matriz_a = [[1, 2], [4, -1]]
matriz_ai = [[0, 0], [0, 0]]
ad = 0

print('Matriz A:')
print()
for coluna in matriz_a:
    print(coluna)

def det2(matriz_a):
    return matriz_a[0][0]*matriz_a[1][1] - matriz_a[0][1]*matriz_a[1][0]

def inv2(matriz):
    d = det2(matriz_a)
    return [[matriz_a[1][1]/d, -matriz_a[0][1]/d], [-matriz_a[1][0]/d, matriz_a[0][0]/d]]

matriz_ai = inv2(matriz_a)
ad = det2(matriz_a)

print()

print('Matriz A Inversa:')
print('=-'* 8)
for linha in range(0, 2):
    for coluna in range(2):
        print('[{:^5.1f}]'.format(matriz_ai[linha][coluna]), end='')
    print()
print('=-'* 8)