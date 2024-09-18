# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO
# SE ELE ULTRAPASSAR A VELOCIDADE DE 80KM/H MOSTRE UMA MENSAGEM QUE ELE FOI MULTADO
# A MULTA VAI CUSTAR R$7.00 POR CADA KM ACIMA DO LIMITE.

import random
limite = 80.0
velocidade = float(random.randint(60,120))
multa =  7

print('VELOCIDADE DO VEÍCULO DETECTADA FOI DE: {} KM/H '.format(velocidade))

if velocidade >= limite:
    print('VOCÊ FOI MULTADO!')
    multa = multa * (velocidade - limite)
    print('MULTA TOTAL: R${:.2f}' .format(multa))
else:
    print('TUDO CERTO!')