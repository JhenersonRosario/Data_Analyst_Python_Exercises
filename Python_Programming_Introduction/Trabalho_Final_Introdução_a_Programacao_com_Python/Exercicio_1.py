lista_nomes=[]
lista_idades=[]
lista_altura=[]

for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa:")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa:"))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa:"))

    lista_nomes.append(nome)
    lista_idades.append(idade)
    lista_altura.append(altura)

maior_idade = lista_idades.index(max(lista_idades))
menor_altura = lista_altura.index(min(lista_altura))
media_idade = sum (lista_idades) / len (lista_idades)

print(f"A pessoa mais velha é {lista_nomes[maior_idade]} e tem {lista_idades[maior_idade]} anos de idade!")
print(f"A pessoa com a menor altura é {lista_nomes[menor_altura]} e tem {lista_altura[menor_altura]} metros de altura!")
print(f"A média das idades das pessoas desta lista é de: {media_idade:.2f}")