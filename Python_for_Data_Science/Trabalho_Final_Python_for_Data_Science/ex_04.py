import pandas as pd

conteudo = pd.read_csv(r"compras.csv", sep=',')

total_mulheres_2014 = conteudo[(conteudo['ano'] == 2014) & (conteudo['sexo'] == 'F')]
quant_mulheres = len(total_mulheres_2014)

print(f"Em 2014 o número total de compras realizadas por mulheres foram de :{quant_mulheres} compras.")

#Resultado : Em 2014 o número total de compras realizadas por mulheres foram de :141 compras.
