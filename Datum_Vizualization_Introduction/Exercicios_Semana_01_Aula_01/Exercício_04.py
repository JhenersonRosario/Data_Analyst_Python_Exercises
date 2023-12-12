import pandas as pd

conteudo = pd.read_csv(r'alunos.csv', sep=',')

filtro = (conteudo['ano'] == 1) | (conteudo['ano'] == 3)
alunos_1_3 = conteudo[filtro]

medias = alunos_1_3.groupby('ano')['nota_semestre_1'].mean()

# Resultado = A média dos alunos do terceiro ano são maiores do que as do primeiro ano.