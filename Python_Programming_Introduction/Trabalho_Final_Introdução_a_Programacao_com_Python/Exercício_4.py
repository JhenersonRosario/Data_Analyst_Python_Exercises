soma_peso_maior = []
soma_peso_menor =[]

for i in range(10):
    idade = int(input(f"Digite a Idade da {i+1}ª pessoa:"))
    peso = float(input(f"Digite o Peso da {i+1}ª pessoa:"))

    if idade >=18:
     soma_peso_maior.append(peso)
    else:
       soma_peso_menor.append(peso)

media_maior = sum(soma_peso_maior) / len (soma_peso_maior)
media_menor = sum(soma_peso_menor) / len (soma_peso_menor)

if media_maior > media_menor:
   print(f"A média de peso é maior entre as pessoas maiores de idade. A média de peso é de {media_maior:.2f} Kg!")
elif media_menor > media_maior:
   print(f"A média de peso é maior entre as pessoas menores de idade. A média de peso é de {media_menor:.2f} Kg!")
else:
   print(f"A média de peso é igual entre as duas faixas etárias!")