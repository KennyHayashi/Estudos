#1 CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME #

nome = str(input('Informe o seu nome: '))

if nome.find('Silva') != -1: # <-- SE O RETORNO DO METODO 'FIND' NA VARIAVEL FOR DIFERENTE DE -1 (NÃO ENCONTRADO)
    print('Você possui "Silva" em seu sobrenome!')
else:
    print('Você NÃO possui "Silva" em seu sobrenome!')

#2 CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO" #

cidade = str(input('Informe a sua cidade: '))

cidade = cidade.split() # <-- REALIZA A DIVISÃO DE UMA LINHA DE CARACTERES ENTRE OS ESPAÇOS VAZIOS E QUEBRA DE LINHA

if cidade[0] !='Santo': # <-- SE O RETORNO DO INPUT NÃO TIVER 'SANTO' NA PRIMEIRA STRING DA LISTA
    print('Sua cidade NÃO começa com o nome "Santo"')
else: print('Sua cidade começa com o nome "Santo"!')