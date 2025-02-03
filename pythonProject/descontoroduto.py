s = str(input("Informe sexo: "))

while s != 'M' or s != 'F':
    print("Valor Inválido, tente novamente.")

if s == 'M':
    print("Sexo MASCULINO!")
else:
    print("Sexo FEMININO")
