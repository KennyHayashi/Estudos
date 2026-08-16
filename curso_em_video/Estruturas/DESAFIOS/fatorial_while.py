# faça um programa que leia um numero qualquer e mostre o seu fatorial ex: 5! = 5x4x3x2x1 = 120 #

n = int(input('Informe um número e mostraremos o seu fatorial: '))
valor_original = n # <- armazena o número digitado para mostrar no print#
fatorial = 1
while n > 0:
   fatorial = fatorial * n
   n = n - 1
print(f'O fatorial do n° {valor_original} é: {fatorial}')
