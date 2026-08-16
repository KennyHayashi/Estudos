# FAÇA UM INPUT QUE LEIA QUALQUER COISA NELE E O PRINT DO MESMO MOSTRE OQUE FOI INFORMADO E SUA TIPAGEM #

something = input('Digite algo: ')

if something.isnumeric(): # <- condicional simples de valor booleano para atribuir uma resposta a variavel 'tipo' #
    tipo = 'numerico'
elif something.isalpha() and something.islower():
    tipo = 'alfabeto e minusculo'
else:
    if something.isalpha() and something.isupper():
        tipo = 'alfabeto e maiusculo'


print('{0}, {1}'.format(something, tipo))


