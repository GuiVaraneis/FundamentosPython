n = str(input("informe seu nome completo: "))
nome = n.split()
print("primeiro nome: {}".format(nome[0]))
print("ultimo nome: {}".format(nome[len(nome)-1]))