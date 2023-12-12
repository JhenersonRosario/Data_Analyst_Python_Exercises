serie = []

while True:
    numeros = int(input("Digite um número para adicionar a série:"))
    if numeros <0:
        break
    serie.append(numeros)

soma = sum (serie)
media = soma / len (serie)
maximo = max(serie)
minimo = min(serie)

print(f"A soma da série de números é: {soma}")
print(f"A média de todos os números da série é:{media}")
print(f"O maior número da série é:{maximo}")
print(f"O menor número da série é:{minimo}")
