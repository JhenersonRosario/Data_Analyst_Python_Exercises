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
    
    media_final = (notas_1 + notas_2 + notas_3 + notas_4) / 4

    if numero_faltas > numero_aulas * 0.25:
        print("Reprovado por Faltas!")
    elif media_final <7 :
        print("Reprovado por Média!")
    else :
        print("Aluno Aprovado!")
    print("")
    opcao = input("Gostaria de verificar e cadastrar as notas de outro aluno ?(s/n) ")
    if opcao.lower() == "n":
        break