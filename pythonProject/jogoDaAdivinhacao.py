import subprocess
from random import randint

i = int(0)

print("JOGO DA ADIVINHAÇÃO")
print("NÚMERO DE TENTATIVAS: {}".format(i))
numeroSecreto = randint(1, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Digite um numero de 1 a 10:"))
    palpites += 1
    if jogador == numeroSecreto:
        print("Você acertou o número secreto! \n")
        acertou = True
    else:
        if numeroSecreto > jogador:
            print("Mais... vamo que vamo!")
        elif numeroSecreto < jogador:
            print("Menos... Dá pra melhorar !!!")
print("Você acertou com {} tentativas".format(palpites))
