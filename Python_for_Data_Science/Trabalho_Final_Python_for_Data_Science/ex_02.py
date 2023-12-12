import pandas as pd

conteudo = pd.read_csv(r"compras.csv", sep=',')

homens = conteudo[(conteudo['sexo'] == 'M')]
mulheres = conteudo[(conteudo['sexo'] == 'F')]

quant_homens = len(homens)
quant_mulheres = len(mulheres)

print(f"A quantidade de Mulheres no banco de dados é de : {quant_mulheres} mulheres.")
print(f"A quantidade de Homens no banco de dados é de : {quant_homens} homens.")


#A quantidade de Mulheres no banco de dados é de : 2142 mulheres.
#A quantidade de Homens no banco de dados é de : 2858 homens.
