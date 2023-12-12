n_termos = int(input("Digite o número de termos desejados:"))

a=1
b=1

print(a)
print(b)

i = 2
while i < n_termos:
    c = a + b
    print (c)
    a = b
    b = c
    i += 1