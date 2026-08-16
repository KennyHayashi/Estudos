''' Crie um programa que leia varios numeros inteiros, o programa só vai parar quando o usuario digitar
999 que é a condição de parada, no final mostre quantos numeros foram digitados e qual foi a soma entre eles
desconsiderando o flag'''


cont = soma = 0

while True:
    nums = int(input('Digite um número: '))
    if nums == 999:
        break
    cont += 1
    soma += nums

print(f'Você digitou {cont} números diferentes de 999, e a soma entre todos os n° digitados foi de: {soma}')
