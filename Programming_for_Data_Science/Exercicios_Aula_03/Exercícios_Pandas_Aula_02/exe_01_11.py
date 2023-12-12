import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'vgsales.csv')

# 1) Jogo mais vendido no mundo em 2010
top_game_2010 = data[data['Year'] == 2010].nlargest(1, 'Global_Sales')
print("1) Jogo mais vendido no mundo em 2010:")
print(top_game_2010[['Name', 'Global_Sales']])
print("\n")

# 2) Gênero mais vendido na América do Norte em 2005
na_sales_2005 = data[(data['Year'] == 2005)]['NA_Sales']
if not na_sales_2005.empty:
    max_na_sales_2005 = na_sales_2005.max()
    top_genre_na_2005 = data[(data['Year'] == 2005) & (data['NA_Sales'] == max_na_sales_2005)]['Genre'].values[0]
    print(f"2) Gênero mais vendido na América do Norte em 2005: {top_genre_na_2005}")
else:
    print("2) Não há dados para o ano de 2005 na América do Norte.")
print("\n")

# 3) Empresa que mais vendeu de 2005 até 2016
top_publisher = data.groupby('Publisher')['Global_Sales'].sum().idxmax()
print("3) Empresa que mais vendeu de 2005 até 2016:", top_publisher)
print("\n")

# 4) Nome do jogo menos vendido em 2008 do gênero Sports
worst_selling_sports_2008 = data[(data['Year'] == 2008) & (data['Genre'] == 'Sports')].nsmallest(1, 'Global_Sales')
print("4) Nome do jogo menos vendido em 2008 do gênero Sports:")
print(worst_selling_sports_2008[['Name', 'Global_Sales']])
print("\n")


# 6) Ano com mais lançamentos de jogos
year_with_most_releases = data['Year'].value_counts().idxmax()
print("6) Ano com mais lançamentos de jogos:", year_with_most_releases)
print("\n")

# 7) Plataforma que menos lançou jogos
platform_with_least_releases = data['Platform'].value_counts().idxmin()
print("7) Plataforma que menos lançou jogos:", platform_with_least_releases)
print("\n")

# 8) Plataforma que mais gerou lucros com jogos do gênero Action desde 2009
top_platform_action = data[data['Year'] >= 2009][data['Genre'] == 'Action'].groupby('Platform')['Global_Sales'].sum().idxmax()
print("8) Plataforma que mais gerou lucros com jogos do gênero Action desde 2009:", top_platform_action)
print("\n")


# 9) Empresa com maior lucro de 1980 a 1995 (excluindo SNES)
top_publisher_1980_1995 = data[(data['Year'] >= 1980) & (data['Year'] <= 1995) & (data['Platform'] != 'SNES')].groupby('Publisher')['Global_Sales'].sum().idxmax()
print("9) Empresa com maior lucro de 1980 a 1995 (excluindo SNES):", top_publisher_1980_1995)
print("\n")

# 10) Verificar se a empresa que mais lucrou no Japão em 2003 é a mesma da Europa
top_publisher_japan_2003 = data[(data['Year'] == 2003) & (data['JP_Sales'] == data['JP_Sales'].max())]['Publisher']
top_publisher_europe_2003 = data[(data['Year'] == 2003) & (data['EU_Sales'] == data['EU_Sales'].max())]['Publisher']

if not top_publisher_japan_2003.empty and not top_publisher_europe_2003.empty:
    same_publisher = top_publisher_japan_2003.values[0] == top_publisher_europe_2003.values[0]
else:
    same_publisher = False

print("10) A empresa que mais lucrou no Japão em 2003 é a mesma que mais lucrou na Europa nesse mesmo ano?", same_publisher)
print("\n")

# 11) Percentual de vendas globais de jogos de Wii (excluindo NA, JP e EU) de 2006 a 2010
wii_sales_other_regions = data[(data['Platform'] == 'Wii') & (data['Year'] >= 2006) & (data['Year'] <= 2010)]['Other_Sales'].sum()
wii_total_sales = data[(data['Platform'] == 'Wii') & (data['Year'] >= 2006) & (data['Year'] <= 2010)]['Global_Sales'].sum()
percent_wii_sales_other_regions = (wii_sales_other_regions / wii_total_sales) * 100
print("11) Percentual relacionado às vendas globais de jogos de Wii (excluindo América do Norte, Japão e Europa) de 2006 até 2010:", percent_wii_sales_other_regions)
print("\n")

