soma = 0 
quant_valores = 0
quant_positivos = 0
quant_negativos = 0
while True:
    valor = int(input("Digite um valor positivo ou negativo (Ou digite 0 para sair do programa):"))
    if valor ==0:
        break
    
    soma += valor
    quant_valores += 1

    if valor < 0 :
        quant_negativos +=1
    else:
        quant_positivos +=1
    
if quant_valores == 0:
    print("Nenhum Valor foi informado")
else:
    media = soma / quant_valores
    percentual_positivos = (quant_positivos / quant_valores)*100
    percentual_negativos = (quant_negativos / quant_valores)*100

print("")
print("A média Aritmética dos valores informados é:{}".format(media))
print("A quantidade de valores positivos é:{}".format(quant_positivos))
print("A quantidade de valores negativos é:{} ".format(quant_negativos))
print("O percentual de valores positivos é:{:.2f}%".format(percentual_positivos))
print("O percentual de valores negativos é:{:.2f}%".format(percentual_negativos))