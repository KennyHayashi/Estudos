# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR #
n1 = int(input('DIGITE UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR: '))
suc = n1 + 1
ant = n1 - 1

print('Você digitou o número de {0}, e seu sucessor é {1} e o seu antecessor é {2}'.format(n1, suc, ant))

# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E SUA RAIZ QUADRADA #
m1 = int(input('INFORME UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E SUA RAIZ QUADRADA: '))
dobro = m1 * 2
triplo = m1 * 3
raiz = int(m1 ** (1/2))

print('Seu Número é {0} e o seu dobro é de {1}, o seu triplo é de {2} e sua raíz quadrada é de {3:.1f}'.format(m1, dobro, triplo, raiz))

# CRIE UM PROGRAMA QUE LEIA AS TRÊS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA #
nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

print('Sua média de nota durante as 3 provas foi de {:.2f}'.format(media))

# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS #
metros = float(input('Informe uma quantidade de metros para converter'))
cent = metros * 100
milimetros = metros * 1000

print('{0} metros serão convertidos em {1} centímetros e/ou {2} milímetros'.format(metros, cent, milimetros))

# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR #
carteira = float(input('Informe seu saldo atual: '))
dolar = float(carteira / 5.66)

print('Seu saldo atual é de {0} e você vai poder adquirir um total de {1} dólares americanos'.format(carteira, dolar))
