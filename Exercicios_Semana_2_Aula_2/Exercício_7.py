valor = 0
maior_valor = 0
menor_valor = float('inf')

for i in range(10):
    valor = float(input("Digite um valor:"))

    if valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor
print(f"O menor valor é de: {menor_valor} e o maior valor é de: {maior_valor}")