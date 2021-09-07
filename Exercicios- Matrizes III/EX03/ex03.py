def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]

matriza = [[3, 4], [2, 3]]

matrizalin = len(matriza)
matrizacol = len(matriza[0])

matrizb = [[-1], [-1]]
matrizblin = len(matrizb)
matrizbcol = len(matrizb[0])

matRes = []

print()
print('Matriz A')
print('=-'* 5)
for j in matriza:
    print(j)
print('=-'* 5)


print()
print('Matriz B')
print('=-'* 5)
for j in matrizb:
    print(j)
print('=-'* 5)
print()



for i in range(matrizalin):
    matRes.append([])

    for j in range(matrizbcol):
        listMult = [x*y for x, y in zip(getLinha(matriza, i), getColuna(matrizb, j))]

        matRes[i].append(sum(listMult))

print('Multiplicação de duas matrizes:')
print('=-'* 5)
for j in matRes:
    print(j)
print('=-'* 5)
print()