import pandas as pd


dataset = pd.read_csv(r'dados.csv')

# 1) Quantidade de pessoas nas faixas etárias
qtd_20_ou_menos = len(dataset[dataset['Idade'] <= 20])
qtd_21_a_35 = len(dataset[(dataset['Idade'] > 20) & (dataset['Idade'] <= 35)])
qtd_36_a_50 = len(dataset[(dataset['Idade'] > 35) & (dataset['Idade'] <= 50)])
qtd_51_a_65 = len(dataset[(dataset['Idade'] > 50) & (dataset['Idade'] <= 65)])
qtd_maiores_65 = len(dataset[dataset['Idade'] > 65])

# 2) Média de escolaridade em cada faixa etária
media_escolaridade_faixa_etaria = dataset.groupby('Idade')['Anos de Estudo'].mean()

# 3) UF com maior renda média
uf_maior_renda = dataset.groupby('UF')['Renda'].mean().idxmax()
#4
# Renda média de pessoas pretas e pardas, separadas por sexo
renda_media_pretos_pardos = dataset[(dataset['Cor'].isin(['Preta', 'Parda']))].groupby(['Cor', 'Sexo'])['Renda'].mean()

# Renda média de pessoas brancas, separadas por sexo
renda_media_brancos = dataset[dataset['Cor'] == 'Branca'].groupby(['Cor', 'Sexo'])['Renda'].mean()


print("1) Quantidade de pessoas nas faixas etárias:")
print(f"a) 20 anos ou menos: {qtd_20_ou_menos}")
print(f"b) 21 a 35 anos: {qtd_21_a_35}")
print(f"c) 36 a 50 anos: {qtd_36_a_50}")
print(f"d) 51 a 65 anos: {qtd_51_a_65}")
print(f"e) Maiores de 65 anos: {qtd_maiores_65}")

print("\n2) Média de escolaridade em cada faixa etária:")
print(media_escolaridade_faixa_etaria)

print("\n3) UF com maior renda média:")
print(uf_maior_renda)

print("4) Renda média de pessoas pretas e pardas, separadas por sexo:")
print(renda_media_pretos_pardos)
print("\nRenda média de pessoas brancas, separadas por sexo:")
print(renda_media_brancos)