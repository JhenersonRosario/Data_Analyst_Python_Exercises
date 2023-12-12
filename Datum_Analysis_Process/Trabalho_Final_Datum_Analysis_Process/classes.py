#Exercício 1 - Criar uma Classe que modele uma bola.
class Bola:
    def __init__(self,cor,cincurferencia,material):
        self.cor = cor
        self.circunferencia = cincurferencia
        self.material = material
    def troca_cor (self,nova_cor):
        self.cor = nova_cor
    def mostra_cor(self):
       return print("A cor da bola é {}".format(self.cor))

#Exercício 2 - Crirar uma Classe que modele 1 retângulo.

class Retangulo:
    
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_lados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def retornar_lados(self):
        return self.ladoA, self.ladoB

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return 2 * (self.ladoA + self.ladoB)

#Exercício 3 - Cria uma classe que implemente uma conta corrente. 
class Conta_Corrente:
    def __init__(self, n_conta, titular, saldo = 0):
        self.n_conta = n_conta
        self.titular = titular
        self.saldo = saldo
    def alterar_nome(self, novo_titular):
        self.titular = novo_titular
    def deposito(self, valor):
    
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Seu novo saldo é de R${self.saldo}.")
        else:
            print("Saldo insuficiente para saque.")

#Exercício 4 - Classe que cria Tamagochi.

class Tamagochi:
    def __init__(self, nome, fome, saude, idade ):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f"O novo nome do seu Tamagochi é :{self.nome}")
    def alterar_fome(self, valor):
        self.fome = valor
    def altear_saude(self, valor):
        self.saude = valor
    def alterar_idade(self, valor):
        self.idade = valor
    def retorna_nome(self):
        print(f"O nome de seu Tamagochi é : {self.nome}")
    def retorna_fome(self):
        print(f"O nível de fome de {self.nome} é de {self.fome}.")
    def retorna_idade(self):
        print(f"A idade de {self.nome} é de {self.idade} anos.")
    def retorna_saude(self):
        print(f"O nível de saúde de {self.nome} é de {self.saude}.")

#Exercício 5 - Bomba de Combustível 
class Bomba:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        quantidade_litros = valor_abastecido / self.valor_litro
        if quantidade_litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= quantidade_litros
            return quantidade_litros
        else:
            return 0

    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return valor_pagar
        else:
            return 0

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel
