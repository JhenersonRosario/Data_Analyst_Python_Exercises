while True :
    produto_un = int(input("Digite a quantidade de produtos comprados:"))
    preco = float(input("Digite o preço do produto que vocÊ comprou:"))
    total = produto_un * preco
    if produto_un <=5 :
        desconto = total * 0.02
    elif produto_un >5 and produto_un <=10 :
        desconto = total * 0.03
    else:
        desconto = total * 0.05
    total_a_pagar = total - desconto
    print("O valor total de sua compra com desconto é de:" ,total_a_pagar)
    opcao = input("Deseja verificar o valor de outro produto ?(s/n)")
    if opcao.lower() == "n":
        break
    
    
