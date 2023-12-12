numero = int(input("Digite um número inteiro para realizar o somatório:"))
soma = 0
for i in range(1, numero+1):
    soma += i

print("A soma dos Números de 1 a {} é {}".format( numero ,soma))

