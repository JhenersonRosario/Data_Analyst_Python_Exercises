funcionarios = []

while True:
    nome = input("Digite o nome do funcionário. Para encerrar o programa digite 'fim': ")
    if nome == "fim":
        break
    valor_salario_hora = float(input("Digite o valor do salário/hora do funcionário:"))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas do funcionário:"))
    funcionarios.append({"nome" : nome, "valor_hora" : valor_salario_hora, "horas_trabalhadas" : horas_trabalhadas }) 

total_horas = 0
total_salario_bruto = 0
total_impostos = 0

for funcionario in funcionarios:
    salario_bruto = funcionario ["valor_hora"] * funcionario ["horas_trabalhadas"]
    total_horas += funcionario["horas_trabalhadas"]
    total_salario_bruto += salario_bruto
    if salario_bruto <= 2999.99 :
        percentual_imposto = 0.1
    elif salario_bruto >= 3000 and salario_bruto <= 5499.99:
        percentual_imposto = 0.13
    elif salario_bruto >= 5500 and salario_bruto <= 7999.99:
        percentual_imposto = 0.16
    else:
        percentual_imposto = 0.2
        
    imposto = salario_bruto * percentual_imposto
    total_impostos += imposto
    salario_liquido = salario_bruto - imposto
    
    funcionario["salario_bruto"] = salario_bruto
    funcionario["percentual_imposto"] = percentual_imposto
    funcionario["imposto"] = imposto
    funcionario["salario_liquido"] = salario_liquido

for funcionario in funcionarios:
    print("Funcionário:", funcionario["nome"])
    print("Salário Bruto: RS{:.2f}".format(funcionario["salario_bruto"]))
    print("Percentual de imposto retido em fonte : {}".format(funcionario["percentual_imposto"]))
    print("Valor do imposto retido na fonte: R$ {:.2f}".format(funcionario["imposto"]))
    print("Salário líquido: R$ {:.2f}".format(funcionario["salario_liquido"]))
    print("")

print("O total de horas trabalhadas foi de : {} horas".format(total_horas))
print("O total da folha de pagamento bruta foi de : R$ {:.2f}".format(total_salario_bruto))
print("O total de impostos foi de : R$ {:.2f}".format(total_impostos))
print("O total da folha de pagamento líquida foi de : R$ {:.2f}".format(total_salario_bruto - total_impostos))
