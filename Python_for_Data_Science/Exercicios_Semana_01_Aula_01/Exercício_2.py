alunos = []
for i in range (5):
    nome = input(f"Digite o nome do {i+1}º aluno:")
    nota_1 = float(input("Digite a nota 1 de {}:".format(nome)))
    nota_2 = float(input("Digite a nota 2 {}:".format(nome)))
    media = (nota_1 + nota_2 ) / 2

    aluno = {
        "nome": nome,
        "nota1":nota_1,
        "nota2":nota_2,
        "media":media,
    }
    alunos.append(aluno)
aprovados =[]

for aluno in alunos:
    if aluno["media"] >=7.0:
        aprovados.append(aluno)
print("Lista de Alunos Aprovados:")
for aluno in aprovados:
    print("{}: {:.1f}".format(aluno["nome"], aluno["media"]))
