n = int(input("Tabuada do: "))

for c in range(0, 11, 1):
    resultado = c * n
    print("{} * {} = {}".format(n, c, resultado))
