matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 2):
       if linha == coluna:
           matriz[linha][coluna] = 1

       else:
            matriz[linha][coluna] = (linha+1) ** 2


for linha in  range (0, 3):
    for coluna in range(0, 2):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()