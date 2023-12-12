import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'vgsales.csv')

# 12) Gráfico de linhas com vendas por plataforma ao longo dos anos
platform_sales_by_year = data.pivot_table(index='Year', columns='Platform', values='Global_Sales', aggfunc='sum')
platform_sales_by_year.plot()
plt.xlabel('Ano')
plt.ylabel('Vendas Globais (em milhões)')
plt.title('Vendas Globais de Jogos por Plataforma ao Longo dos Anos')
plt.legend(title='Plataforma', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 13) Gráfico de pizza com o percentual de vendas por gênero
genre_sales = data.groupby('Genre')['Global_Sales'].sum()
plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Percentual de Vendas por Gênero de Jogos')
plt.show()