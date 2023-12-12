import pandas as pd

conteudo = pd.read_csv(r"compras.csv", sep=',')

compras_credito_2010 = conteudo[(conteudo['ano'] == 2010) & (conteudo['pagamento'] == 'credito')]
total_cred_2010 = len(compras_credito_2010)

print(f"Em 2010 o número total de compras realizadas no crédito foram de :{total_cred_2010} compras.")

#Resultado : Em 2010 o número total de compras realizadas no crédito foram de :82 compras.
