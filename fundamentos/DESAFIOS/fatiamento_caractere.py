# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA QUE MOSTRE:
  #1 - O NOME COM TODAS AS LETRAS MAIUSCULAS ;
  #2 - O NOME COM TODAS AS LETRAS MINUSCULAS ;
  #3 - QUANTAS LETRAS AO TOTAL FORAM IDENTIFICAS ( SEM CONSIDERAR ESPAÇOS )
  #4 - QUANTAS LETRAS TEM O PRIMEIRO NOME ;

nome = input('Informe o seu nome completo: ')

nome = nome.upper() # <-- FORMATA PARA DEIXAR TODAS A STRING EM MAIUSCULA
print('#1', nome) # <-- OU print(nome.upper()) // PARA SINGLE PRINT (SEM ALTERAR O VALOR FINAL DA VARIAVEL)

nome = nome.lower() # <-- FORMATA PARA DEIXAR TODAS A STRING EM MINUSCULA
print('#2', nome)

#nome = nome.replace('x', 'y') # <-- SUBSTITUI ESPAÇOS INDESEJAVEIS DA STRING POR OUTRO ARGUMENTO
print('#3', len(nome.replace(' ', '')))

nome = nome.split( ) # <-- REALIZA A DIVISÃO DA CADEIA DE CARACTERES DA STRING E CRIA UMA LISTA
print('#4', len(nome[0]))

