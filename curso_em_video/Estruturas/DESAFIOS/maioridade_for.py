# filtro simples para diferenciar maioridade baseado no A/D/N do usuario ex pra fixar o loop for #

maior = menor = 0

for c in range(0, 7):
    idade = int(input('Informe seu ano de nascimento: '))
    if (2026 - idade) < 18:
        menor += 1
    elif (2026 - idade) > 18:
        maior += 1
print('{} pessoas atingiram a maioridade e {} não atingiram a maioridade' .format(maior, menor))

