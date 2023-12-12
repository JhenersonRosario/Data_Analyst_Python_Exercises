altura_chico = 1.50
crescimento_chico = 0.02
altura_Ze = 1.10
crescimento_Ze = 0.03
anos = 0

while altura_Ze < altura_chico:
    altura_chico += crescimento_chico
    altura_Ze += crescimento_Ze
    anos +=1

print("A quantidade de anos necessários até Zé ser maior que Chico é:" ,anos)