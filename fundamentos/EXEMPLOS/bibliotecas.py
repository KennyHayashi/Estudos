#BIBLIOTECAS#

#caso importe a biblioteca utilizando FROM, não há necessidade de adicionar math.(comando), apenas a sua função

from math import sqrt, ceil
num = int(input('Informe um número:  '))
raiz = sqrt(num)
print('A raíz do número: {0} é igual a: {1:.0f}'.format(num, ceil(raiz)))

#math.ceil --> arredonda valor númerico para cima //math.floor --> arredonda valor númerico para baixo

#--------------------------------------------------------------------------------------------------------------

import random # <-- módulo de uma biblioteca que randomiza números automaticamente
num = random.randint(1,100) # <-- ranint = para números inteiros

print(num)