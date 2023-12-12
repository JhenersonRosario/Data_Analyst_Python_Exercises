#c) Crie um programa que utilize esta classe. Ele deve pedir
#ao usuário que informe as medidas de um local. Depois,
#deve-se criar um objeto com as medidas e calcular a
#quantidade (em m2) de pisos (1 x 1 m2) e de rodapés
#necessários para o local.

from classes import Retangulo

local_a = float(input("Informe a medida do Lado A do Local: "))
local_b = float(input("Informe a media do Lado B do Local: "))

local = Retangulo(local_a, local_b)

area_local = local.calcula_area()
perimetro_local = local.calcula_perimetro()

quantidade_pisos = area_local
quantidade_rodape = perimetro_local

print("A quantidade de pisos necessários é: {} m²")
print("A quantidade de pisos necessários é: {} m²")