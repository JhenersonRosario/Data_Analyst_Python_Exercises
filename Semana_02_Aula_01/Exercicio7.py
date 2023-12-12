while True:

    temperatura = float(input("Digite a temperatura atual do ambiente:"))

    if temperatura <=15:
        print("MUITO FRIO")
    elif temperatura >=16 and temperatura <=22:
        print("FRIO")
    elif temperatura >=23 and temperatura <=26:
        print("AGRADÁVEL")
    elif temperatura >=27 and temperatura <=30:
        print("QUENTE")    
    else:
        print("MUITO QUENTE")

    opcao = input("Deseja testar outra temperatura? (s/n) ")

    if opcao.lower() == "n":
        break
