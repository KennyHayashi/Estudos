# DESENVOLVE UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM #
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM #
# E R$0,45 PARA VIAGENS MAIS LONGAS QUE 200KM

distancia = int(input('Informe a KM de sua viagem: '))
passagem = float(0.50)


print('Você vai viajar {} KM'.format(distancia))

if distancia > 200:
    passagem = 0.45
    total = distancia * passagem
    print('Será cobrado um valor de R${:.2f} por KM '.format(passagem))
    print('O valor total da sua passagem será de: R${:.2f} '.format(total))
else:
    total = distancia * passagem
    print('Será cobrado um valor de R${:.2f} por KM '.format(passagem))
    print('O valor total da sua passagem será de: R${:.2f} '.format(total))