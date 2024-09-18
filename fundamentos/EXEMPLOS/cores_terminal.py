# CORES NO TERMINAL #

#exemplos de cores abaixo:
#\033[0;30;41m (sem estilização; texto na cor branca; fundo vermelho)
#\033[4;33;44m (sublinhado; texto na cor amarela; fundo azul marinho)
#\033[1;35;43m (negrito; texto da cor roxa; fundo amarelo)
#\033[30;42m   (sem estilização; texto na cor branca; fundo verde)
#\033[m        (sem estilização; texto na cor padrão; sem fundo) ~ padrão
#\033[7;30m    (inversão de cores; texto na cor preto; sem fundo)
#print('exemplo\033[m') (formatação para a cor de fundo acompanhar o limite do texto)

print('\033[30;42mteste\033[m') # <- foi realizada a formatação das cores e estilos;