num_N = int(input("Digite o Valor de N:"))
soma = 0
for i in range (1, num_N+1):
    m = 2*i - 1
    termo = i / m
    soma += termo
    print("{}/{} ".format(i,m), end="")
print("\n\nSoma dos termos: {:.2f}".format(soma))