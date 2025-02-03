salario = float(input("Qual o salário do funcionário?: R$ "))
novoSalario = salario + ((salario*15)/100)

print("Salário reajustado: R${:.2f}".format(novoSalario))
