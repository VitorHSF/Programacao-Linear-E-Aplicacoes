from time import sleep

matriz_a = [[2, 1], [-3, 4]]
matriz_b = [[0, -1], [2, 5]]
matriz_c = [[3, 0], [6, 1]]
resultado_matriz = [[0, 0], [0, 0]]
matriz_ct = list(map(list, zip(*matriz_c)))

print('|----------FATEC AMERICANA-----------|')
print('|Análise E Desenvolvimento De Sistema|')
print('|---Programação Linear E Aplicação---|\n')

print('------------==------------')
print('calcule: [A + (B – CT)] * B')
print('------------==------------\n')

print('Matriz A:')
for coluna in matriz_a:
    print('{}'.format(coluna))


print('\nMatriz B:')

for coluna in matriz_b:
    print('{}'.format(coluna))


print('\nMatriz C:')

for coluna in matriz_c:
    print('{}'.format(coluna))
print()

for linha in range(0, 2):

    for coluna in range(0, 2):
        resultado_matriz[linha][coluna] = matriz_b[linha][coluna] - matriz_ct[linha][coluna]

for linha in range(0, 2):

    for coluna in range(0, 2):
        resultado_matriz[linha][coluna] = matriz_a[linha][coluna] + resultado_matriz[linha][coluna]

for linha in range(0, 2):

    for coluna in range(0, 2):
        resultado_matriz[linha][coluna] = resultado_matriz[linha][coluna] * matriz_b[linha][coluna]

print()
print('Resultado Do Cálculo: Matriz [A + (B-C^T)] * B =')
print('calculando.')
sleep(2.0)
print('calculando..')
sleep(1.5)
print('calculando...\n')
sleep(1.0)

sleep(1.0)
print('=-'* 8)


for linha in range(0, 2):
    for coluna in range(0, 2):
        print('[{:^4}]'.format(resultado_matriz[linha][coluna]), end='')
    print()
print('=-'* 8)