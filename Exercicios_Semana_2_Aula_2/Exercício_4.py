
soma_salario = 0
soma_filhos = 0
maior_salario = 0
cont_salario_2k = 0


for i in range(5):
   salario = float(input("Digite o salário da pessoa:"))
   filhos = int(input("Digite a quantidade de filhos da pessoa:"))



soma_salario += salario
soma_filhos += filhos


if salario > maior_salario:
   maior_salario = salario
if salario <= 2000:
   cont_salario_2k +=1



media_salario = soma_salario / 5
media_filhos = soma_filhos / 5

porcentagem_2k = (cont_salario_2k / 5) *100

print(f"A média de salário é:{media_salario:.2f}")
print("A média do número de filhos é:",media_filhos)
print("O maior salário é de R$:",maior_salario)
print(f"O percentual de pessoas com salário até R$2000 é:{porcentagem_2k:.2}")