numeros_negativos = 0 

for i in range(5):
    valor = float(input("Digite um valor:"))
    if valor <0 :
        numeros_negativos +=1

print(f"A quantidade de números negativos é: {numeros_negativos}") 
