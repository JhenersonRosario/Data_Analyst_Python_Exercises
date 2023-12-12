faturamento = float(input("Digite o Faturamento da Empresa:"))
lucro = faturamento * 0.32
if faturamento <5000:
    imposto = lucro * 0.12
elif faturamento >=5000 and faturamento< 15000:
    imposto = lucro * 0,18
else:
    imposto = lucro * 0.30

valor_total_pos_imposto = lucro - imposto

print(f"O valor total a pagar de imposto é de :R${imposto:.2f}")
print(f"O valor do lucro é de :R${lucro:.2f}")
print(f"O valor total do lucro após o desconto de impostos é de :R${valor_total_pos_imposto:.2f}")

