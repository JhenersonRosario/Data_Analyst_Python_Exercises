#Versão que tentei criar englobando todos os requisitos das questões 10 A e B em um só código tentando abranger todas as possibilidades de sucesso ou fracasso do aluno!
while True:
    print("Bem vindo ao sistema de notas do aluno!")
    print("")
    notas_1 = float(input("Digite as notas do 1º Bimestre:"))
    notas_2 = float(input("Digite as notas do 2º Bimestre:"))
    notas_3 = float(input("Digite as notas do 3º Bimestre:"))
    notas_4 = float(input("Digite as notas do 4º Bimestre:"))
    print("")

    numero_aulas = int(input("Digite o número total de aulas:"))
    numero_faltas = int(input("Digite o número total de faltas:"))
    frequencia = ((numero_aulas - numero_faltas) / numero_aulas) * 100
    media_final = (notas_1 + notas_2 + notas_3 + notas_4) / 4

    if numero_faltas > numero_aulas * 0.25:
        print("Reprovado por Faltas!")
    elif media_final <7 :
        print("Reprovado por Média!")
    elif media_final >= 5 and media_final < 7 and frequencia >= 75:
        print("Em Recuperação!")
    elif numero_faltas > numero_aulas * 25 and media_final <7 :
        print("Aluno REPROVADO por Faltas e por Média!")
    else:
        print("Aluno Aprovado")

    print("")
    opcao = input("Gostaria de verificar e cadastrar as notas de outro aluno ?(s/n) ")
    if opcao.lower() == "n":
        break