from Dados import load_data
import matplotlib.pyplot as plt 

alunos = load_data(r'alunos.csv', ',')

soma_semestre_1 = 0
soma_semestre_2 = 0

for aluno in alunos:
    soma_semestre_1 = soma_semestre_1 + aluno ['nota_semestre_1']
    soma_semestre_2 = soma_semestre_2 + aluno ['nota_semestre_2']


# Definir os Rótulos e os Valores das colunas
rotulos = ['Semestre 1' , 'Semestre 2']
valores = [soma_semestre_1 , soma_semestre_2]
# Criando o gráfico de colunas/barras
plt.bar(rotulos, valores)

# Adicionando rótulos aos eixos
plt.xlabel('Semestre')
plt.ylabel('Soma das Notas')
# Adicionando título ao gráfico
plt.title('Soma das notas')
#Exibir o Gráfico
plt.show()