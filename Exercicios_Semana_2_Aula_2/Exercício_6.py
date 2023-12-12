candidato_1 = 0
candidato_2 = 0
voto_nulo = 0
voto_branco = 0

for i in range(5):
    print("Digite 1 para votar no Candidato 1.")
    print("Digite 2 para votar no Candidato 2.")
    print("Digite 3 para votar Nulo.")
    print("Digite 4 para votar Em Branco.")
    print("")
    escolha = int(input("Digite a opção desejada:"))

    if escolha == 1:
        candidato_1 += 1
    elif escolha ==2:
        candidato_2 += 1
    elif escolha == 3:
        voto_nulo += 1 
    else:
        voto_branco += 1
print(f"O Candidato 1 teve a quantidade total de : {candidato_1} votos")
print(f"O Candidtato 2 teve a quantidade total de : {candidato_2} votos")
print(f"A quantidade de votos Nulos foi: {voto_nulo}")
print(f"A quantidade de votos Em Branco foi: {voto_branco}")
