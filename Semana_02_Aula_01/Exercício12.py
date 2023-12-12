dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    fevereiro = 29
else:
    fevereiro = 28


if mes == 2:
    dias_mes = fevereiro
elif mes in [4, 6, 9, 11]:
    dias_mes = 30
else:
    dias_mes = 31


if dia > dias_mes:
    print("Data inválida.")
else:

    if dia == dias_mes:

        if mes == 12:
            dia = 1
            mes = 1
            ano += 1
        else:
            dia = 1
            mes += 1
    else:
        dia += 1
    
    print("Data do próximo dia:", dia, "/", mes, "/", ano)
