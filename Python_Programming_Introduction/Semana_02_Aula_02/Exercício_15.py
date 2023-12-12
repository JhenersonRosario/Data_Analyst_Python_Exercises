numero = int(input("Digite o número entre 1 a 10 o qual deseja saber a tabuada:"))

for i in range(1,11):
    print("{} x {} = {}".format(numero , i , numero*i))