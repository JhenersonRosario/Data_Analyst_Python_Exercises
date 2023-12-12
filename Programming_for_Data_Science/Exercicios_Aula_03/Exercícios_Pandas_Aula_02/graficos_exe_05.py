import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'vgsales.csv')


# 5) Gráfico com o total de vendas por ano
sales_by_year = data.groupby('Year')['Global_Sales'].sum()
plt.plot(sales_by_year.index, sales_by_year.values)
plt.xlabel('Ano')
plt.ylabel('Vendas Globais (em milhões)')
plt.title('Vendas Globais de Jogos por Ano')
plt.show()