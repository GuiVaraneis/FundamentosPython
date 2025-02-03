valor = float(input("Qual o valor do produto? R$ "))

desconto = valor*15/100
novoValor = valor - desconto

print("Valor do produto: R${}".format(valor))
print("Desconto R${}".format(desconto))
print("Valor final R${}".format(novoValor))

