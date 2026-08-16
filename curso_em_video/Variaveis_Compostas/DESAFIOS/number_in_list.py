# crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista #
# caso o numero ja exista la dentro, ele nao sera adicionado #
# no final mostre todos os valores unicos digitados em ordem crescente #

valores = list()
nums = 0

while True:
    nums = (int(input('Digite um valor: ')))
    if nums not in valores:
        valores.append(nums)
    else:
        print(f'o numero {nums} já foi informado e não será adicionado a lista!')
    continuar = str(input('Deseja Continuar? [s] ou [n]: ')).upper()
    if continuar == 'N':
        break

valores.sort()

print(valores)