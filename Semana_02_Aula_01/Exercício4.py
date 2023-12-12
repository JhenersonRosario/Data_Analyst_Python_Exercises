numero = int(input("Digite um numero inteiro de três dígitos:"))

centenas = numero // 100
dezena = (numero % 100) // 10
unidade = numero %10 

print("O número de centenas é:" ,centenas)
print("O número de dezenas é:" ,dezena)
print("O número de unidades é:",unidade)

