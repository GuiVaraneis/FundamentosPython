n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))

print("""[ 1 ] SOMAR 
         [ 2 ] MULTIPLICAR 
         [ 3 ] MAIOR
         [ 4 ] NOVOS NUMEROS
         [ 5 ] SAIR DO PROGRAMA""")
opcao = str(input("Qual propriedade matemática deseja?: "))

while opcao != 5:
    if opcao == 1:
        print("Somatória {}".format(n1+n2))
    elif opcao == 2:
        print("Multiplicação {}".format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print("O primeiro valor é maior")
        elif n2 > n1:
            print("O segundo valor é maior")
        else:
            print("os dois valores são iguais")
    elif opcao == 4:
        print("Insira os valores novamente: ")
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    elif opcao == 5:
        print("Encerrando")
    else:
        print("opção inválida")
