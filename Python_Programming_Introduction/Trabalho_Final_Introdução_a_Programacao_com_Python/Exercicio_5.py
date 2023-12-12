altura_p1 = 1.85
idade_p1 = 56
crescimento_p1 = 0.03
altura_p2 = 1.64
idade_p2 = 35
crescimento_p2 = 0.045
anos = 0

while altura_p1 >= altura_p2 and idade_p1 <=110 and idade_p2 <=110:
    altura_p1 += crescimento_p1
    idade_p1 +=1
    altura_p2 += crescimento_p2
    idade_p2 += 1
    anos += 1

print(f"Serão necessários {anos} anos para que a Pessoa 2 ultrapasse a altura da Pessoa 1!")
print(f"Atualmente a Pessoa 1 estaria com {idade_p1} anos e a Pessoa 2 estaria com {idade_p2} anos de idade !")
print(f"Atualmente a altura da Pessoa 1 é de {altura_p1} metros de altura e a pessoa 2 estaria com {altura_p2} ")
