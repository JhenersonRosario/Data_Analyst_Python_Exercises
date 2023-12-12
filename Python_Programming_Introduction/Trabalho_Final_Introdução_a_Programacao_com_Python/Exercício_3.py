
preco_ingresso_a = 5.00
despesas_pessoa_a = 0.30
preco_ingresso_b = 5.50
despesas_pessoa_b = 0.50
publico_a = [150, 180]
publico_b = [150, 180]

for i in range(2):
    faturamento_a = publico_a[i] * preco_ingresso_a
    lucro_a = faturamento_a - (publico_a[i] * despesas_pessoa_a)
    despesas_gerais_a = publico_a[i] * despesas_pessoa_a
    print(f"Show {i+1} (Cenário A):")
    print(f"Faturamento: R${faturamento_a:.2f}")
    print(f"Lucro: R${lucro_a:.2f}")
    print(f"Despesas gerais: R${despesas_gerais_a:.2f}")
    print("")

    faturamento_b = publico_b[i] * preco_ingresso_b
    lucro_b = faturamento_b - (publico_b[i] * despesas_pessoa_b)
    despesas_gerais_b = publico_b[i] * despesas_pessoa_b
    print("")
    print(f"Show {i+1} (Cenário B):")
    print(f"Faturamento: R${faturamento_b:.2f}")
    print(f"Lucro: R${lucro_b:.2f}")
    print(f"Despesas gerais: R${despesas_gerais_b:.2f}")
