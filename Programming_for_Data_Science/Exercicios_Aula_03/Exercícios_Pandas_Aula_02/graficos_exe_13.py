import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'vgsales.csv')

# 13) Gráfico de pizza com o percentual de vendas por gênero
genre_sales = data.groupby('Genre')['Global_Sales'].sum()
plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Percentual de Vendas por Gênero de Jogos')
plt.show()