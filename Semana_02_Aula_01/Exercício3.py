while True:
    idade = int(input("Digite quantos anos você tem:(ou digite - 1 para sair)"))
    if idade == -1:
        print("Saindo do Programa")
        break
    elif idade >= 18:
        print("Maior de Idade")
    elif idade <=0 or idade >=120:
        print("Idade Inválida, tente novamente:")
    else:
        print("Menor de idade")