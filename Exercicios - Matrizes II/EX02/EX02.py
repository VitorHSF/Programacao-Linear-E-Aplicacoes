from time import sleep

matriz_a  = [[2, 1], [-3, 4]]
matriz_b  = [[0, -1], [2, 5]]
matriz_c  = [[3, 0], [6, 1]]
resultado_matriz  = [[0, 0], [0, 0]]

matrizci = [[0, 0], [0, 0]]
resultado_matrizB = [[0, 0], [0, 0]]
Resultado_matriz3B = [[0, 0], [0, 0]]

print('|----------FATEC AMERICANA-----------|')
print('|Análise E Desenvolvimento De Sistema|')
print('|---Programação Linear E Aplicação---|')


print('\n|-----------------==-----------------|')
print('calcule: (B + AT) * C-1 – (3* BT)')
print('|-----------------==-----------------|\n')

matriz_at= list(map(list, zip(*matriz_a)))
print('Matriz A:')
for coluna in matriz_a:
    print('{}'.format(coluna))
print()

matriz_bt= list(map(list, zip(*matriz_b)))
print('Matriz B:')
for coluna in matriz_b:
    print('{}'.format(coluna))
print()

print('Matriz C')
for coluna in matriz_c:
    print('{}'.format(coluna))
print()

def det2(matriz_c):
    return matriz_c[0][0]*matriz_c[1][1] - matriz_c[0][1]*matriz_c[1][0]

def inv2(matriz_c):
    d = det2(matriz_c)
    return [[matriz_c[1][1]/d, -matriz_c[0][1]/d], [-matriz_c[1][0]/d, matriz_c[0][0]/d]]

matriz_ci = inv2(matriz_c)
for linha in range(0, 2):
    for coluna in range(0, 2):
        resultado_matrizB[linha][coluna] = matriz_b[linha][coluna] + matriz_at[linha][coluna]

for linha in range(0, 2):
    for coluna in range(0, 2):
        Resultado_matriz3B[linha][coluna] = 3 * matriz_bt[linha][coluna]

for linha in range(0, 2):
    for coluna in range(0, 2):
        resultado_matriz[linha][coluna] = resultado_matrizB[linha][coluna] * matriz_ci[linha][coluna]

for linha in range(0, 2):
    for coluna in range(0, 2):
        resultado_matriz[linha][coluna] = resultado_matriz[linha][coluna] - Resultado_matriz3B[linha][coluna]

print()
print('Resultado Cálculo \nMatriz (B + A^T) * C^-1 -(3 * B^T) =')

print('\ncalculando.')
sleep(1.0)
print('calculando..')
sleep(0.5)
print('calculando...\n')
sleep(0.3)

print('=-'* 14)
for linha in range(0, 2):
    for coluna in range(0, 2):
        print('[{:^10.1f}]'.format(resultado_matriz[linha][coluna]), end='')
    print()
print('=-' * 14)
