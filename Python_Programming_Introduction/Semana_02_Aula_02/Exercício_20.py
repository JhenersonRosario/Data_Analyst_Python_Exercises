A = int(input("Digite o Valor de início da sequência:"))
R = int(input("Digite o Valor da Razão da sequência:"))

for i in range(1,10):
    calculo = A * pow(R, i-1)
    print("Termo" , i,"=", calculo)
    