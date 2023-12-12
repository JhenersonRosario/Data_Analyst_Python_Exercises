preco_unidade = 5.40  
desconto_percentual = 0.5 
qtd_comprada = int(input("Quantas unidades do produto foram compradas? "))

valor_total_sem_desconto = qtd_comprada * preco_unidade
print(f"Valor total da compra (sem desconto): R$ {valor_total_sem_desconto:.2f}")

qtd_centenas = qtd_comprada // 100
print(f"Quantidade de centenas compradas: {qtd_centenas}")

valor_desconto = valor_total_sem_desconto * (desconto_percentual / 100) * qtd_centenas
print(f"Desconto: R$ {valor_desconto:.2f}")

valor_total_com_desconto = valor_total_sem_desconto - valor_desconto
print(f"Valor total da compra (com desconto): R$ {valor_total_com_desconto:.2f}")
