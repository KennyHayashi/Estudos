#CRIE UM PROGRAMA QUE LEIA VARIOS N° E COLOQUE EM UMA LISTA#
# A) QUANTOS N° FORAM DIGITADOS
# B) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE
# C) SE O VALOR 5 FOI DIGITADO E ESTA OU N NA LISTA #

lista = list()
contador = 0
check = str('')

while True:
    lista.append(int(input('Informe um número: ')))
    continuar = str(input('Deseja continuar? [s] / [n]')).upper()
    contador += 1
    if 5 in lista:
        check = str('o n° 5 foi digitado e está na lista!')
    else:
        check = str('o n° 5 NÃO foi digitado e NÃO está na lista!')
    if continuar == 'N':
        break

lista.sort(reverse=True)

print(f'Foram digitados {contador} números, lista decrescente: {lista}, {check}')
