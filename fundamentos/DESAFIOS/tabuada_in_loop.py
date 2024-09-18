#   TABUADA COM LOOP  #

n = int(input('Digite um número para criar uma tabuada: '))
tab = 1
res = n * tab

print('{0} x {1} = {2}'.format(n, tab, res))

while tab <= 10:
    tab += 1
    res = n * tab
    print('--------------')
    print('{0} x {1} = {2}'.format(n, tab, res))
    if tab == 10:
        break