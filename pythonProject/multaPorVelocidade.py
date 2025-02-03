velocidade = int(input("Informe velocidade percorrida pelo carro: "))
if velocidade > 80:
    print("multado!\nValor da multa: {}".format(velocidade*7))
else:
    print("Está dentro do limite de velocidade.")
