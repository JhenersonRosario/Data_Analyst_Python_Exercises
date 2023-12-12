altura_mulheres = []
altura_homens = []

while True:
    altura = float(input("Digite a Altura da pessoa:"))

    if altura <0:
        break
    sexo = input("Digite o Sexo da Pessoa: (M)Masculino (F)Feminino:").upper()
    if sexo == 'M':
        altura_homens.append(altura)
    elif altura == 'F':
        altura_mulheres.append(altura)

media_feminina = 1.60
media_masculina = 1.73

mulheres_acima_media = sum(altura > media_feminina for altura in altura_mulheres)
mulheres_abaixo_media = sum(altura < media_feminina for altura in altura_mulheres)
homens_acima_media = sum(altura > media_masculina for altura in altura_homens)
homens_abaixo_media = sum(altura < media_masculina for altura in altura_homens)

print(f"{mulheres_acima_media} mulheres estão acima da média nacional de altura!")
print(f"{mulheres_abaixo_media} mulheres estão abaixo da média nacional de altura!")
print(f"{homens_acima_media} homens estão acima da média nacional de altura!")
print(f"{mulheres_abaixo_media} homens estão abaixo da média nacional de altura!")
