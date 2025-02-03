import random

um = str(input("Nome do primeiro aluno: "))
dois = str(input("Nome do segundo aluno: "))
tres = str(input("Nome do terceiro aluno: "))
quatro = str(input("Nome do quarto aluno: "))

lista = [um, dois, tres, quatro]

print("O aluno escolhido foi {}".format(random.shuffle(lista)))
