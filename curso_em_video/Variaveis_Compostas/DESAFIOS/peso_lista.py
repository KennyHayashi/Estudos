# faça um programa que leia nome e peso de varias pessoas em uma lista, no final mostre: #
# a) quantas pessoas foram cadastradas #
# b) uma listagem com as pessoas mais pesadas #
# c) uma listagem com as pessoas mais leves #

pessoas = list()
dados = list ()
total = 0
mpesado = 85
mleve = 70
lista_pesado = list()
lista_leve = list()

while True:
    pessoas.append(str(input('Informe o nome: ')))
    pessoas.append(int(input('Informe o peso: ')))
    continuar = str(input('Deseja continuar? [s] / [n]? -> ')).upper()

    dados.append(pessoas[:])
    pessoas.clear()
    total += 1

    if continuar == 'N':
        break

for i in dados:
    if i[1] >= mpesado:
        lista_pesado.append(i[0])
    if i[1] <= mleve:
        lista_leve.append(i[0])

print(f'Foram cadastradas: {total} pessoas!')
print(f'Pessoas mais pesadas: {lista_pesado}')
print(f'Pessoas mais leves: {lista_leve}')


