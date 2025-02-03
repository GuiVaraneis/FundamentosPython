import random

scoreRecorde = 0
vitorias = 0
ganhou = True

while ganhou:
    print(f"Maior sequência de vitórias: {scoreRecorde}\n")
    print(f"TOTAL DE VITÓRIAS: {vitorias}\n")
    print("Vamos jogar Par ou Impar!\n")
    eu = str(input("Você deseja ser Par ou impar?(P para par, I para Impar): "))
    eu = eu.upper()

    opcComputador = str

    if eu == 'P':
        print("Você selecionou Par!\n")
    elif eu == 'I':
        print("Você selecionou Ímpar!\n")

    jogador = int(input("SUA VEZ!: "))
    jogador2 = random.randint(0, 100)
    print(f"MINHA VEZ!:  {jogador2}")
    resultadoFinal = jogador + jogador2

    print(f"{jogador} + {jogador2} = {resultadoFinal}")

    if resultadoFinal % 2 == 0 and eu == 'P':
        print("PAR! VOCÊ VENCEU :)\n")
        vitorias += 1
    elif resultadoFinal % 2 != 0 and eu == 'I':
        print("IMPAR! VOCÊ VENCEU! :)\n")
        vitorias += 1
    elif resultadoFinal % 2 != 0 and eu == 'P':
        print("IMPAR! VOCÊ PERDEU! :(\nFIM DE JOGO!!!\n")
        ganhou = False
    elif resultadoFinal % 2 == 0 and eu == 'I':
        print("PAR! VOCê PERDEU! :(\nFIM DE JOGO!!!\n")
        ganhou = False
    if vitorias > scoreRecorde:
        scoreRecorde = vitorias
        print(f"NOVO RECORDE DE SEQUÊNCIA!{scoreRecorde} VITÓRIAS!\n")
    if not ganhou:
        opc = input("Deseja jogar novamente? (S - PARA JOGAR NOVAMENTE): ")
        opc = opc.upper()
        if opc == 'S':
            ganhou = True
            vitorias = 0
        else:
            print("Encerrando...\n")
