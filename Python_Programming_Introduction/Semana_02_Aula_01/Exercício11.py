dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    fevereiro = 29
else:
    fevereiro = 28

if mes == 2:
    if dia > fevereiro:
        print("Data inválida.")
    else:
        print("Data válida.")
elif mes in [4, 6, 9, 11]:
    if dia > 30:
        print("Data inválida.")
    else:
        print("Data válida.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia > 31:
        print("Data inválida.")
    else:
        print("Data válida.")
else:
    print("Mês inválido.")