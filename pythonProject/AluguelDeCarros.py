km = float(input("Quilômetros percorridos: "))
dias = int(input("Dias percorridos: "))

Total = ((60*dias) + (km*0.15))

print("total: {:.2f}".format(Total))
