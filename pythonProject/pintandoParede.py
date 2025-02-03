h = float(input("Informe altura da parede: "))
l = float(input("Informe largura da parede: "))
area = h * l
print("A dimensão da parede é {}x{} e sua área é de {:.2}m².\n ".format(h, l, area))
tinta = area / 2
print("para pintar essa parede, você precisará de {:.2} de tinta".format(tinta))

