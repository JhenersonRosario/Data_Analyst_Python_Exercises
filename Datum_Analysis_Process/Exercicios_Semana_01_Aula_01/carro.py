from classes import Carro


meu_fusca = Carro(15)


meu_fusca.adicionar_gasolina(20)

meu_fusca.andar(100)


nivel_gasolina = meu_fusca.obter_gasolina()
print(f"Nível de gasolina: {nivel_gasolina}")