from classes import Retangulo

print("Informe as medidas do local:")
lado_a = float(input("Lado A:"))
lado_b = float(input("Lado B:"))

retangulo = Retangulo(lado_a, lado_b)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

quantidade_pisos = int(area)
quantidade_rodapes = int(perimetro)

print(f"A quantidade de m² de pisos necessária é de: {quantidade_pisos} m² ")
print(f"A quantide de m² de rodapés necessários é de : {quantidade_rodapes} m²")
