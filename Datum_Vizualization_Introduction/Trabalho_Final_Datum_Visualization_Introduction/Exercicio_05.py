from Dados import load_data
import matplotlib.pyplot as plt

alunos = load_data(r'alunos.csv' , ',')
total_alunos = len(alunos)
cont_media_7 = 0
cont_mais_15_faltas = 0
cont_media_menor_7 = 0

for aluno in alunos:
    nota_semestre_1 = aluno.get('nota_semestre_1', 0)
    nota_semestre_2 = aluno.get('nota_semestre_2', 0)
    media = nota_semestre_1 + nota_semestre_2 / 2
    faltas = aluno.get('faltas')
    if media > 7:
            cont_media_7 += 1
            if faltas > 15:
              cont_mais_15_faltas += 1
    if media < 7:
         cont_media_menor_7 +=1
mais_15_faltas = cont_mais_15_faltas
media_7 = cont_media_7
media_7_abaixo_15f = media_7 - mais_15_faltas


# Criação do Gráfico
total_alunos_str = f'Total de Alunos: {total_alunos} ({total_alunos/total_alunos*100:.1f}%)'
media_7_str = f'Alunos > 7 abaixo 15 Faltas: {media_7_abaixo_15f} ({media_7_abaixo_15f/total_alunos*100:.1f}%)'
media_7_abaixo_15f_str = f'Alunos > 7 com mais de 15 Faltas: {media_7 - media_7_abaixo_15f} ({(media_7 - media_7_abaixo_15f)/total_alunos*100:.1f}%)'
media_menor_7_str = f'Alunos < 7: {cont_media_menor_7} ({cont_media_menor_7/total_alunos*100:.1f}%)'

rotulos = [media_7_str, media_7_abaixo_15f_str, media_menor_7_str]
valores = [media_7_abaixo_15f, media_7 - media_7_abaixo_15f, cont_media_menor_7]

fig1, ax1 = plt.subplots()

ax1.pie(valores, labels=rotulos, autopct='%1.1f%%', shadow=True, startangle=90)

ax1.axis('equal')
plt.title('Distribuição de Médias dos Alunos')
plt.figtext(0.5, 0.05, total_alunos_str, ha='center', fontsize=12)

plt.show()

