import pandas as pd

conteudo = pd.read_csv(r'alunos.csv', sep=',')

filtro = conteudo['escola'] == 'Pedro II'
escola_pedro = conteudo[filtro]

media_faltas_pedro_II = escola_pedro['faltas'].mean()

print(f"A média de faltas dos alunos da Escola Pedro II é:{media_faltas_pedro_II:.2f}")

# RESULTADO : A média de faltas dos alunos da Escola Pedro II é:15.34

