#2) Qual foi o percentual de alunos que utilizaram e que não utilizaram a monitoria?

import matplotlib.pyplot as plt
from Dados import load_data

alunos = load_data(r'alunos.csv' , ',')
alunos_monitoria_true = 0
alunos_monitoria_false = 0

for aluno in alunos:
    if aluno['monitoria'] == True:
        alunos_monitoria_true +=1
    else:
        alunos_monitoria_false += 1

porcentagem_monitoria_true = (alunos_monitoria_true / len(alunos) ) *100
porcentagem_monitoria_false = (alunos_monitoria_false / len(alunos) )*100

#Criação do conjunto de dados 
rotulos = ['Alunos que fizeram monitoria' , 'Alunos que não fizeram Monitoria']
valores = [porcentagem_monitoria_true, porcentagem_monitoria_false]

#Representação, área de plotagem
fig1 , ax1 = plt.subplots()

#Criação do gráfico
ax1.pie(valores, labels=rotulos, autopct='%1.1f%%' , shadow= True, startangle= 90)

ax1.axis('equal')

#Mostragem do gráfico
plt.show()