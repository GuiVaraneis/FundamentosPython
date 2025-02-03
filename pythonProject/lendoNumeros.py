n = s = 0
i = 0
while True:
    n = int(input('Digite um número(-1 para parar: '))
    if n == -1:
        break
    s += n
    i += 1
print(f'A quantidade de número digitados foi: {i}\nA soma total dos números informados é: {s}')
