import pandas as pd

conteudo = pd.read_csv(r'alunos.csv')

alunos_media_7 = conteudo[(conteudo['nota_semestre_1'] + conteudo['nota_semestre_2']) / 2 >= 7]
alunos_acima_15 = alunos_media_7[alunos_media_7['faltas'] > 15]

quant_acima_15 = len(alunos_acima_15)

print(f"A quantidade de Alunos que obtiveram a média igual ou maior a 7, ultrapassando o parâmetro de 15 faltas é: {quant_acima_15} alunos")

#A quantidade de Alunos que obtiveram a média igual ou maior a 7, ultrapassando o parâmetro de 15 faltas é: 439 alunos