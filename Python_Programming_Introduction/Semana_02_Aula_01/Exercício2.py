while True:
    numero = int(input("Digite um número(Ou digite 0 para sair):"))
    if numero == 0:
        break
    else:
        if numero %2 == 0:
            print("O número é par!")
        else:
            print("O número é ímpar!")