from Dados import load_data
import matplotlib.pyplot as plt
alunos = load_data(r'alunos.csv' , ',')

soma_notas_ano_1 = 0
soma_notas_ano_3 = 0

for aluno in alunos:
    if aluno['ano'] == 1:
        soma_notas_ano_1 += aluno['nota_semestre_1']
    elif aluno['ano'] == 3:
        soma_notas_ano_3 += aluno['nota_semestre_1']

rotulos = [' 1º Ano', '3º Ano']
valores = [soma_notas_ano_1 , soma_notas_ano_3]
cores = ['red' , 'blue']

plt.bar(rotulos, valores , color = cores)
plt.xlabel ('Turmas')
plt.ylabel ('Média das Notas')
plt.title ('Comparativo Entre a Média das Turmas')
plt.show()