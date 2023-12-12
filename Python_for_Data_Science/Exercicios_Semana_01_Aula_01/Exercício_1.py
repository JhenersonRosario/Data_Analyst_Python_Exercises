lista_numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º numero da lista :"))
    lista_numeros.append(num)

lista_numeros_reverse = list(reversed(lista_numeros))
print(f"A lista de números que você digitou em ordem reversa é:{lista_numeros_reverse}")

