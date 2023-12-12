import pandas as pd

conteudo = pd.read_csv(r"compras.csv", sep=',')

jovens = conteudo[(conteudo['idade'] >=18) & (conteudo['idade']<=25)]
adultos = conteudo[(conteudo['idade'] >=26) & (conteudo['idade']<=59)]
idosos = conteudo[(conteudo['idade'] >=60)]

quant_jovens = len(jovens)
quant_adultos = len(adultos)
quant_idosos = len(idosos)

if quant_jovens > quant_adultos and quant_jovens > quant_idosos:
    print(f"A faixa etária que mais realizou compras no banco de dados foram os Jovens (18 a 25 anos) com um total de : {quant_jovens} compras.")
elif quant_adultos > quant_jovens and quant_adultos > quant_idosos:
        print(f"A faixa etária que mais realizou compras no banco de dados foram os Adultos (26 a 59 anos) com um total de : {quant_adultos} compras.")
else:
      print(f"A faixa etária que mais realizou compras no banco de dados foram os Idosos (60 anos +) com um total de :{quant_idosos} compras.")


#Resultado : A faixa etária que mais realizou compras no banco de dados foram os Adultos (26 a 59 anos) com um total de : 3280 compras.
