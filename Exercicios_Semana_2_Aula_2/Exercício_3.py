import math
numero = int(input("Digite um número inteiro e positivo:"))
E = 1
fatorial = 1
for i in range(1, numero+1):
    fatorial *= i
    E += 1/fatorial
print(f"O Valor de E é:{E:.2f}")