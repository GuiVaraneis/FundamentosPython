from math import pow

a = int(input("Valor do primeiro cateto: "))
b = int(input("valor do segundo cateto: "))

print("Aplicando o teorema de pitágoras...")
print("{}² + {}² = {}5".format(a, b, pow(a, 2)+pow(b, 2)))
