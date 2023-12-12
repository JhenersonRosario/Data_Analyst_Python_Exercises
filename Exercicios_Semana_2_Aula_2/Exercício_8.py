idade = []
salario = []
n_jovens = 0
n_adultos = 0
n_idosos = 0
acum_salarios_jov = 0
acum_salarios_adult = 0
acum_salario_idosos = 0

for i in range(10):
    idade = int(input("Digite a Idade da pessoa:"))
    salario = float(input("Digite o Salario da Pessoa:"))
    idade.append(idade)
    salario.append(salario)
    
    if idade <18:
        n_jovens +=1
        acum_salarios_jov +=1
    elif idade >=18 and idade <60:
        n_adultos +=1
        acum_salarios_adult +=1
    else:
        n_idosos +=1
        acum_salario_idosos +=1

media_idade = sum(idade) / len(idade)
print(f"A média de Idades é de {media_idade:.2f} ")

if acum_salarios_jov > acum_salarios_adult and acum_salarios_jov > acum_salario_idosos:
    maior_salario = "jovens"
elif acum_salarios_adult > acum_salarios_jov and acum_salarios_adult > acum_salario_idosos:
    maior_salario = "adultos"
else:
    maior_salario = "idosos"

print(f"Há {n_jovens} jovens , {n_adultos} adultos e {n_idosos} idosos trabalhando.")
print(f"A faixa etária que acumula é: {maior_salario} ")