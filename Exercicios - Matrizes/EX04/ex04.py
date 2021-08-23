from time import sleep

matriz = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
matrizresult = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrizt= list(map(list, zip(*matriz)))
print('=-=' * 20)

print('Dada a Matriz A, obtenha a matriz B tal que B = A + At')

print('\nMatriz A:')
for j in matriz:
    print('{}'.format(j))
print()

print('Matriz A Transposta:')
for j in matrizt:
    print(j)

for linha in range(0, 3):

    for coluna in range(0, 3):
        matrizresult[linha][coluna] = matriz[linha][coluna] + matrizt[linha][coluna]

print()

print('calculando.')
sleep(2.0)
print('calculando..')
sleep(1.5)
print('calculando...')
sleep(1.0)

print('\nMatriz B = A + A Transposta:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matrizresult[linha][coluna]), end='')

    print()
print('=-=' * 20)