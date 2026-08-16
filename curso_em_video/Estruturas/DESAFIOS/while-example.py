
while True:
    sex = str(input('Informe o seu sexo: [M] Masculino --- [F] Feminino: ')).upper()
    if sex != 'M' and sex != 'F':
        print('Digite corretamente!')
    else:
        break
print(sex)

