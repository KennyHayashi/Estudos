# crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista #
# ja na posição corretão de inserção ( sem utilizar a função sort() ), no final mostre a lista ordenada #

numbers = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > numbers[-1]: # sempre considera o 1° valor informado como o maior #
        numbers.append(n)
    else:
        pos = 0
        while pos < len(numbers): # loop para comparar todos os valores baseado na posição da lista #
            if n <= numbers[pos]:
                numbers.insert(pos, n) # insere o valor do n na posição correta após comparar #
                break
            pos += 1
print(numbers)
