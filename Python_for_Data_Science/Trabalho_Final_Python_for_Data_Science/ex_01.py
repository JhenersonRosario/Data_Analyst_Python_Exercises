import pandas as pd

conteudo = pd.read_csv(r"compras.csv", sep=',')

jovens = conteudo[(conteudo['idade'] >=18) & (conteudo['idade']<=25)]

quant_jovens = len(jovens)

print(f"A quantidade de pessoas jovens no banco de dados é de:{quant_jovens} pessoas")


#Resultado : A quantidade de pessoas jovens no banco de dados é de:728 pessoas