import pandas as pd

conteudo = pd.read_csv(r'alunos.csv', sep=',')

semestre_1_soma = conteudo['nota_semestre_1'].sum()
semestre_2_soma = conteudo['nota_semestre_2'].sum()

if semestre_1_soma > semestre_2_soma:
    print(f"O maior somatório de notas é do Primeiro Semestre, com uma pontuação total de : {semestre_1_soma} pontos.")
else:
    print(f"O maior somatório de notas é do Segundo Semestre, com uma pontuação total de: {semestre_2_soma} pontos.")

#RESULTADO : O maior somatório de notas é do Segundo Semestre, com uma pontuação total de: 25139.07 pontos.