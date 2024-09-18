# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR #

import random

num = random.randint(0,999)
par = num % 2

print(num)

if par == 0:
    print('O número informado é PAR!')
else:
    print('O número informado é ÍMPAR!')