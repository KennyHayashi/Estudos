

lanches = ('Hamburguer','Suco', 'Pizza', 'Pudim')

print (lanches[2]) #para referenciar qual posição deve ser extraida da tupla, utilizamos '[]' colchetes #

# é possivel tbm fazer o fatiamento das tuplas utilizando o comando  abaixo #

print(lanches[1:3])
# referenciando a posição 1 'suco' até a posição 3'pudim' porem só ira ler 1:2 devido a regra de fatiamento#

for cont in range(0, len(lanches)):
    print(f'Escolhi :{lanches[cont]} na posição {cont} USANDO LEN') # NÃO É MUITO RECOMENDADO #
#loop for num range de 0 a len(comprimento da tupla (lanches) = 4 #
# printe a tupla lanches referenciando a posição utilizada na função len #

# também é possivel utilizar o for da seguinte maneira usando o metodo ENUMERATE #

for pos, comida in enumerate(lanches): # METODO MAIS UTILIZADO/COERENTE DE USAR #
    print(f'Escolhi: {comida} na posição {pos} USANDO ENUMERATE')