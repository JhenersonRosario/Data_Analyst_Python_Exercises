import math

numero = int(input("Digite um valor inteiro:"))
fatorial = 1
for i in range(1, numero+1):
    fatorial *= i

print(f"O Resultado do Fatorial é:{fatorial}")
