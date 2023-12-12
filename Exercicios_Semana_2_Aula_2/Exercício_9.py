destinos = ['Rio de Janeiro', 'Bahia', 'Minas Gerais']
pessoas = {}


for i in range(10):
    nome = input(f'Digite o nome da pessoa {i+1}: ')
    destino = input(f'Digite o destino visitado por {nome} (1-Rio de Janeiro, 2-Bahia, 3-Minas Gerais): ')
    pessoas[nome] = destinos[int(destino)-1]


contagem_destinos = {destino:0 for destino in destinos}
for destino in pessoas.values():
    contagem_destinos[destino] += 1


destino_mais_visitado = None
destino_menos_visitado = None
for destino in destinos:
    if destino_mais_visitado is None or contagem_destinos[destino] > contagem_destinos[destino_mais_visitado]:
        destino_mais_visitado = destino
    if destino_menos_visitado is None or contagem_destinos[destino] < contagem_destinos[destino_menos_visitado]:
        destino_menos_visitado = destino


print(f'O destino mais visitado foi {destino_mais_visitado}.')
print(f'O destino menos visitado foi {destino_menos_visitado}.')