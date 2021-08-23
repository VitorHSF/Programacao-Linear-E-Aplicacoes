print('-='*15)
cpf = input('Digite o seu CPF:')

if (cpf[3] != "."):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")

elif (cpf[7] != "."):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")

elif (cpf[11] != "-"):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")

else:
    print("O CPF digitado '{}' é válido !".format(cpf))