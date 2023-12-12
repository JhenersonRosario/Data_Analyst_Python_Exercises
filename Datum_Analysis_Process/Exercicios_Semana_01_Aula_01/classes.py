class Bola:
    def __init__(self,cor,circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def mostra_cor(self):
        print("A cor da bola é: {}".format(self.cor))
    
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
   
    def muda_valor(self,nova_base,nova_altura):
        self.base = nova_base
        self.altura = nova_altura
    
    def retorna_valor(self):
        print("O valor da base é :{}".format(self.base))
        print("O valor da altura é:{}".format(self.altura))
    
    def calcula_area(self):
       area = self.base * self.altura
       print("A área do Retângulo é: {}" .format(area))
    
    def calcula_perimetro(self):
       perimetro = 2 * (self.base + self.altura)
       print("O perímetro do Retângulo é : {}" .format(perimetro))
    
    def encontrar_centro(self):
        x_centro = self.base / 2
        y_centro = self.altura / 2
        return Ponto(x_centro, y_centro)
    
    
        
class conta:
    def __init__(self,numero,nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def altera_nome(self,novo_nome):
        self.nome = novo_nome
    
    def deposito(self,valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso. Saldo atual de: R$ {self.saldo} ")
    
    def saque(self,valor):
        if self >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Saldo atual de: R$ {self.saldo}")
        else:
            print(f"Saldo insuficiente para realizar o saque. Seu saldo é de:{self.saldo}")

class Tamagotchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}")
        else:
            print("Quantidade de combustível insuficiente")

    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Valor a ser pago: R$ {valor_pagar:.2f}")
        else:
            print("Quantidade de combustível insuficiente")

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Combustível insuficiente para percorrer a distância desejada.")

    def obter_gasolina(self):
        return self.combustivel

    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade