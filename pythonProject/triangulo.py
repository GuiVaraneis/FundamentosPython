print("informe três valores e saiba se os mesmo formam um triangulo")

l1 = int(input("Primeiro lado: "))
l2 = int(input("Segundo lado: "))
l3 = int(input("Terceiro lado: "))
if l1 + l2 < l3 and l1 + l3 < l2 and l2 + l3 < l1:
    print("PODEM FORMAR UM TRIANGULO!\n")

    print("Tipo de triangulo: ")
    if l1 == l2 and l2 == l3 and l3 == l1:
        print("TRIANGULO EQUILÁTERO")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("TRIANGULO ESCALENO")
    else:
        print("TRIANGULO ISÓSCELES")

else:
    print("NÃO PODEM FORMAR UM TRIÂNGULO")
