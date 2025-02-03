c = 0
soma = int(0)
cont = 0
for c in range(1, 7):
    num = int(input("Informe o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Numeros pares: {}\nSoma total: {}\n".format(cont, soma))