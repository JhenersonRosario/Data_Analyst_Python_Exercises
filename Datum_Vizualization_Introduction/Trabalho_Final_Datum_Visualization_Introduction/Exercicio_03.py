import matplotlib.pyplot as plt
from Dados import load_data


dados = load_data(r'alunos.csv', ',')

faltas_escola = {}
alunos_escola = {}

for aluno in dados :
    escola = aluno['escola']
    if faltas_escola.get(escola) != None :
        faltas_escola[escola] += aluno['faltas']
        alunos_escola[escola] +=1
    else:
        faltas_escola [escola] = aluno['faltas']
        alunos_escola[escola] = 1

nomes_escola = list(faltas_escola.keys())
medias = [faltas_escola[escola] / alunos_escola[escola] for escola in nomes_escola]

colors = ['blue' , 'green' , 'red' , 'black']
#Criação Gráficos
plt.bar(nomes_escola, medias , color = colors)

plt.xlabel ('Nome da Escola Escola')
plt.ylabel ('Média de Faltas')
plt.title ('Média de Faltas Entre Escolas')

plt.show()

