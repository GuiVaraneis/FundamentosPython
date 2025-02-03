#informar o ano de nascimento e verificar se o usuário pode ou não pode se alistar
ano = int(input("Informe o ano de nascimento: "))
idade = int(2024 - ano)

if idade > 18:
    print("idade: {}\nJá se passou o tempo de alistamento!".format(idade))
elif idade - ano < 18:
    print("idade: {}\nVocê ainda vai se alistar ao serviço militar".format(idade))
else:
    print("idade: {}\nVocê já pode se alistar".format(idade))
