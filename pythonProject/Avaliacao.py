n1 = float(input("informe nota 1: "))
n2 = float(input("informe nota 2: "))

media = float(n1+n2)/2

if media < 5.0:
    print("MÉDIA FINAL: {}\nSituacão: REPROVADO")
elif 5.0 < media < 6.9:
    print("MÉDIA FINAL: {}\nSituacão: RECUPERAÇÃO ")
else:
    print("MÉDIA FINAL: {}\nSituacão: APROVADO")
