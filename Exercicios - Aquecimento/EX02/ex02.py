def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
c = float(input('Digite o valor do produto R$'))
t = float(input('Digite a taxa de imposto R$'))
print('Valor com imposto R$',somaImposto(t,c))