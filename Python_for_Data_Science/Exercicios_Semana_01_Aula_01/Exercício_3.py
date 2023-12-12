alunos = []
for i in range (5):
    nome = input(f"Digite o nome do {i+1}º aluno:")
    nota_1 = float(input("Digite a nota 1 de {}:".format(nome)))
    nota_2 = float(input("Digite a nota 2 {}:".format(nome)))
    media = (nota_1 + nota_2 ) / 2

    aluno = {
        "nome": nome,      
        "media":media,
    }
    alunos.append(aluno)

for aluno in alunos:
    if aluno["media"] >=7.0:
        print("{}".format(aluno["nome"]))
numero_alunos = len([aluno for aluno in alunos if aluno["media"] >=7.0])

print("{} alunos tiveram a média maior ou igual a 7.0".format(numero_alunos))
