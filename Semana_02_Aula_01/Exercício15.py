nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

print("Notas: {:.1f} e {:.1f}".format(nota1, nota2))
print("Média: {:.1f}".format(media))
print("Conceito: {}".format(conceito))

if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")
