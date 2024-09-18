# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0-5 E PEÇA PARA O USUÁRIO TENTAR
# DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELA MÁQUINA, O PROGRAMA DEVERA MOSTRAR SE O USUARIO ACERTOU OU NÃO!

import random
num = random.randint(0,5) # <-- BIBLIOTECA PARA GERAR UM NÚMERO PSEUDO-ALEÁTORIO
n = int(input('Tente adivinhar o número: '))

print('O número escolhido pela máquina foi o n°{}' .format(num))
if num == n:
    print('Parábens!! Você acertou :) ')
else:
    print('Oppss.. Não foi dessa vez! Tente Novamente :( ')

