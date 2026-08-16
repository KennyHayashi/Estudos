# faça um código que filtre por numeros impares e que são multiplos de 3 ao mesmo tempo #
c = 0

for c in range(1, 100):
    if c%2 != 0 and c%3 == 0:
        print('Este número é impar e multiplo de 3 --> ', c)
    c+=c






