valores = []

for i in range(10):
    valor = float(input("Digite o valor desejado:"))
    valores.append(valor)
soma = sum(valores)

print("A soma de todos os elementos é:" ,soma)
