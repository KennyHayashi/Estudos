# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 - 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADAMENTE #

num = str(input('Informe um número de 0 - 9999: '))

num = num.zfill(4) # <-- METÓDO QUE PREENCHE COM ZEROS Á ESQUERDA PARA GARANTIR QUE TENHA 4 DIGITOS INFORMADOS

print('Número informado é: ', num)

print('Unidade: {0}\nDezena: {1}\nCentena: {2}\nMilhar: {3}'.format(num[3], num[2], num[1], num[0]))
# ^-- FORMATADO PARA SEGUIR A ORDEM DE PRECEDENCIA INFORMADO NO INPUT PELO USUARIO

# FAÇA UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
#1 - QUANTAS VEZES APARECE A LETRA "A"
#2 - EM QUE POSIÇÃO ELA APARECE NA LISTA PELA PRIMEIRA VEZ
#3 - EM QUE POSIÇÃO ELA APARECE NA LISTA NA ÚLTIMA VEZ

frase = str(input('Digite uma frase qualquer: '))

print ('A letra "a" apareceu: ', frase.count('a'))
print('A letra apareceu pela primeira vez na posição: {0} e na última vez: {1}'.format(frase.find('a'), frase.rfind('a')))