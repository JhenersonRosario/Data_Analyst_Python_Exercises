import pandas as pd

conteudo = pd.read_csv(r'alunos.csv', sep=',')

monitoria = conteudo['monitoria']
monitoria_true = 0

for valor in monitoria:
    if valor == True:
        monitoria_true +=1

porcentagem_monitoria =(monitoria_true / len(conteudo))*100

print(f"A porcentagem de alunos que realizaram a monitoria foi:{porcentagem_monitoria:.2f}% dos alunos.")

#RESULTADO : A porcentagem de alunos que realizaram a monitoria foi:49.56% dos alunos.