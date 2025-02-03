s = float(input("informe salário: "))

if s > 1250:
    print("Valor reajustado: R${}".format(s+(s*(10/100))))
else:
    print("Valor reajustado: R${}".format(s+(s*(15/100))))
