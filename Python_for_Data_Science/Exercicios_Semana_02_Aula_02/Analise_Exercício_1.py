lista = []
quant_mulheres = 0
quant_homens = 0
gasto_anual = {}
ano_maior_gasto = None
valor_maior_gasto = 0
maior_gasto_cred = {}
ano_maior_gasto_credito_h = None
maior_valor_cred_h = 0
maior_gasto_total = 0
pessoa_maior_gasto = None
 

nome_arquivo = 'compras.csv'
arquivo = open(nome_arquivo, 'r')
conteudo = arquivo.readlines()
conteudo.remove(conteudo[0])

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].replace('\n' , '')
    formatado = conteudo[i].split(',')
    lista.append({
        'nome': formatado[0],
        'sobrenome': formatado[1],
        'idade':int(formatado[2]),
        'sexo': formatado[3],
        'compra':float(formatado[4]),
        'ano':int(formatado[5]),
        'pagamento':formatado[6],
    })
#1) Qual a porcentagem de homens e mulheres na base de dados?
for i in lista:
    if i['sexo'] == 'F':
        quant_mulheres += 1
    elif i['sexo'] == 'M':
        quant_homens += 1

porcentagem_mulheres = (quant_mulheres / len(lista)*100)
porcentagem_homens = (quant_homens / len(lista)*100)

#2) Qual foi o gasto por ano?
for i in lista:
    ano = i['ano']
    compra =i['compra']
    if ano in gasto_anual:
        gasto_anual [ano] += compra
    else:
     gasto_anual[ano] = gasto_anual.get(ano, 0) + compra
#3)Qual foi o ano com maior gasto?
for ano , gasto in gasto_anual.items():
    if gasto > valor_maior_gasto:
        valor_maior_gasto = gasto
        ano_maior_gasto = ano

#4)Qual foi o ano que os homens mais gastaram em crédito:
for i in lista:
    if i['sexo'] == 'M' and i['pagamento'] == 'credito':
        ano = i['ano']
        compra =i['compra']
        if ano in maior_gasto_cred:
            maior_gasto_cred [ano] += compra
        else:
            maior_gasto_cred [ano] = compra
for ano, gasto in maior_gasto_cred.items():
    if gasto > maior_valor_cred_h:
        maior_valor_cred_h = gasto
        ano_maior_gasto_credito_h = ano

#5)Qual foi a pessoa que mais gastou ?
for pessoa in lista:
    if pessoa['compra'] > maior_gasto_total:
        maior_gasto_total = pessoa['compra'] 
        pessoa_maior_gasto = pessoa['nome'] + ' ' + pessoa['sobrenome']



 
    
  

    
#prints
print("A porcentagem de Homens na lista é de : {porcentagem_homens:.2f}%")
print(f"A porcentagem de Mulheres na lista é de: {porcentagem_mulheres:.2f}%")
for gasto, ano in gasto_anual.items():
    print(f"Gasto no ano de {gasto}:R${ano:.2f}")

print(f"{ano_maior_gasto} foi o ano de maior gasto, tendo um total de gastos de :R$ {valor_maior_gasto:.2f} ")
print(f"O de maior gasto dos homens com a forma de pagamento crédito foi: {ano_maior_gasto_credito_h} com um total de {maior_valor_cred_h:.2f}")
print(f"{pessoa_maior_gasto} foi a pessoa que mais gastou , realizando um total de : R${maior_gasto_total:.2f}")