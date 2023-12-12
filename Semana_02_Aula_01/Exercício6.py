while True:
    numero1 = int(input("Insira o primeiro número:"))
    numero2 = int(input("Insira o segundo número:"))
    print("Para realizar a SOMA dos números digite 1.")
    print("Para realizar a SUBTRAÇÃO dos números digite 2.")
    print("Para PARAR de usar o programa digite 0.")
    opcao = int(input("Escolha a sua opção:"))
    if opcao == 1:
       soma = numero1 + numero2 
       print("O resultado da soma dos números é:" ,soma)
    elif opcao == 2:
       subtracao = numero1 - numero2
       print("O resultado da subtração dos números é:" ,subtracao)
    elif opcao == 0:
       break
    else:
       print("Opção inválida. Por favor tente novamente.")
        


