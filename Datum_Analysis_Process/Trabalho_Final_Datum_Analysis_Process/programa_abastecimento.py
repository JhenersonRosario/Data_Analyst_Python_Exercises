from classes import Bomba


bomba = Bomba("Gasolina", 4.89, 1000)


valor_abastecido = 50.0
litros_abastecidos = bomba.abastecer_por_valor(valor_abastecido)
print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")


litros_abastecidos = 20.0
valor_pagar = bomba.abastecer_por_litro(litros_abastecidos)
print(f"O valor a pagar é de R$ {valor_pagar}.")


novo_valor_litro = 5.0
bomba.alterar_valor(novo_valor_litro)


novo_tipo_combustivel = "Etanol"
bomba.alterar_combustivel(novo_tipo_combustivel)


nova_quantidade_combustivel = 800.0
bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)