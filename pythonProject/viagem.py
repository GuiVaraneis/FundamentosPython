d = int(input("distancia da viagem(em Km): "))
if d <= 200:
    print("Valor da viagem(cobrado o valor de 0.50 por Km): R${}".format(d*0.50))
else:
    print("Valor da viagem(cobrado o valor de 0.45 por Km): R${}".format(d*0.45))
    