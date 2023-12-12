lista_1 = []
lista_2 = []

for i in range(10):
    numero_1 = int(input("Digite um valor para a lista 1:"))
    numero_2 = int(input("Digite um valor para a lista 2 :"))
    lista_1.append(numero_1)
    lista_2.append(numero_2)

lista_3 = []
for i in range(20):
    if i % 2 == 0 :
        lista_3.append(lista_1 [i // 2])
    else:
        lista_3.append(lista_2[i // 2])
print("Lista 1:",lista_1)
print("Lista 2:",lista_2)
print("Lista 3:",lista_3)