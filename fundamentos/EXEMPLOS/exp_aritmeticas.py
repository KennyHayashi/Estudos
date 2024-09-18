# EXPRESSÕES ARITMÉTICAS #

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
elevado = n1 ** n2

# {:.3f} <---- Utilizado para formatação casas decimais de um valor #
# end=' ' <--- Utilizado para não quebrar a linha durante o printl, sem ultrapassar os limites da linha do código #
# \n <--- Utilizado para quebrar uma linha durante uma mesma linha de código #

print('A soma dos valores da {0}, A multiplicação dos valores da {1}, A divisão dos valores da {2:.3f}' .format(soma, mult,div ))
print('A divisão inteira dos valores da {0}, A elevação/potência dos valores da {1}' .format(div_int, elevado))

