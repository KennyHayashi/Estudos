# desenvolva um programa que leia quatro valores e guarde-os em uma tupla, no final mostre:

# a) quantas vezes apareceu o valor 9;
# b) em que posição foi digitado o primeiro valor 3;
# c) quais foram os números pares;

n = ()
pares = ()
for i in range(5):
    valor = int(input('Digite um número: '))
    n += (valor, )
    if valor %2 == 0:
        pares += (valor, )

print(n)
print(f'O valor 9 apareceu: {(n).count(9)}')
if 3 in n:
    print(f'O valor 3 foi digitado primeiro na posição: {(n).index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os números pares digitados foram: {(pares)}')
