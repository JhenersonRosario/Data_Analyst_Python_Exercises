import random

numeros_aleatorios = [random.randint(0, 9) for _ in range(3)]

palpite = input("Digite seu palpite com três números entre 0 e 9 (sem espaços): ")

numeros_coincidentes = 0
for i in range(3):
    if int(palpite[i]) == numeros_aleatorios[i]:
        numeros_coincidentes += 1

if numeros_coincidentes == 0:
    pontos = 0
elif numeros_coincidentes == 1:
    pontos = 10
elif numeros_coincidentes == 2:
    pontos = 100
else:
    if sorted(list(palpite)) == sorted(numeros_aleatorios):
        pontos = 1000000
    else:
        pontos = 1000

print("Números aleatórios: ", numeros_aleatorios)
print("Seu palpite: ", palpite)
print("Pontos: ", pontos)