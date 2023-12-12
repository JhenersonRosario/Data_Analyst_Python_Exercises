from classes import BombaCombustivel


bomba = BombaCombustivel("Gasolina", 5.0, 100.0)


bomba.abastecer_por_valor(50)  

bomba.abastecer_por_litro(10)  

bomba.alterar_valor(4.8)  

bomba.alterar_combustivel("Etanol")

bomba.alterar_quantidade_combustivel(80.0)