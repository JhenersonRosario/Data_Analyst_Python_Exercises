import random

tabuleiro = [[0 for _ in range(20)] for _ in range(20)]

navios = 0
while navios < 20 :
    x = random.randint (0, 19)
    y= random.randint (0, 19 )

    if tabuleiro [x] [y] == 0:
        tabuleiro [x] [y] = 1
        navios += 1


nivel = 0
while nivel not in [1, 2 , 3 , 4]:
    print("Qual o nível que você deseja jogar ?")
    print("(1)Fácil (2)Médio (3)Difícil (4)Informações")
    nivel = int(input("Defina o nível do jogo:"))
    if nivel == 4:
        print("O seu objetivo é destruir todos os 20 navios! Para isso use coordenadas X e Y determinadas por números inteiros de 1 a 19")
        print("No nível Fácil você terá um total de 50 tentativas!")
        print("No nível Médio você terá um total de 40 tentativas!")
        print("No nível Difícil você terá um total de 35 tentativas")
        print("")
        nivel = 0

if nivel == 1:
    total_tentativas = 50
elif nivel == 2:
    total_tentativas = 40
else:
    total_tentativas = 35

print ("Você está jogando no nível {} e terá um total de {} tentativas!".format(nivel , total_tentativas))

acertos_na_agua = 0
acertos_navios = 0
acertos_consecutivos = 0
acertos_atuais = 0

for rodada in range (1 , total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    x = int(input("Digite a coordenada X (0 - 19):"))
    y = int(input("Digite a coordenada Y (0 - 19):"))
    if tabuleiro [x][y]:
        print("Você Acertou um navio!")
        navios -= 1
        tabuleiro [x][y] = 0
        acertos_navios += 1
        acertos_atuais +=1
        if acertos_atuais > acertos_consecutivos:
            acertos_consecutivos = acertos_atuais
    
    else:
        print("Você acertou a água!")
        acertos_na_agua +=1
        acertos_atuais = 0
    rodada += 1
    if navios == 0:
        print("Parabéns!!! Você Destruiu todos os Navios!!!")
        break
    if rodada == total_tentativas:
        print("Game Over!")
        break
porcentagem_acertos_agua = acertos_na_agua / total_tentativas * 100
porcentagem_acertos_navios = acertos_navios/20 * 100

print("O número de acertos na água foi:{}".format(acertos_na_agua))
print("O Número de acertos em navios de:{}".format(acertos_navios))
print("A porcentagem de acertos na água foi de: {:.2f}%".format(porcentagem_acertos_agua))
print("A porcentagem de acertos em navios foi de: {:.2f}%".format(porcentagem_acertos_navios))