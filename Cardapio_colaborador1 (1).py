import os
os.system("cls||clear")
import time

carrinho_de_compra=[]
lista_selecao = []

#Informando valores:
def cardapio_apresentacao():
    print(""" 
   ===== INFORME O NUMERO DO ITEM SELECIONADO =====\n
    N°     |    ALIMENTO    |  VALOR  |
          
    1      |Picanha         | 25,90R$ |
    2      |Lasanha         | 20,90R$ |
    3      |Strogonoff      | 18,90R$ |
    4      |Bife acebolado  | 15,90R$ |
    5      |Feijoada        | 50,90R$ |
    6      |Macarronada     | 19,90R$ |
    7      |Bebidas         | 05,90R$ |
        """)
    
#Valores dos pratos:   
def codigo_card(a):
    if a == 1:
        picanha = 25.90
        return picanha
    elif a == 2:
        lasanha = 20.90
        return lasanha
    elif a == 3:
        strogonoff = 18.90
        return strogonoff
    elif a == 4:
        bife_acebolado = 15.90
        return bife_acebolado
    elif a == 5:
        feijoada = 50.90
        return feijoada
    elif a == 6:
        macarronada = 19.90 
        return macarronada
    elif a == 7:
        bebidas = 05.90
        return bebidas

#Forma de pagamento:
def finalizando_compra (a, b):
    desconto = (sum(b))*0.1
    if a == 1:
        #Debito
        soma = sum(b)
        desconto = 0
        return soma, desconto
    elif a == 2:
        #Crédito
        soma = sum(b)
        result = soma + (desconto)
        return result, desconto
    elif a == 3:
        #Dinheiro
        soma = sum(b)
        result = soma - desconto
        return result, desconto
    elif a == 4:
        #Pix
        soma = sum(b)
        result = soma - desconto
        return result, desconto

#Pratos selecionados:        
def pratos_selecionados(a):
    itens_selecionados=[]
    for lista_itens in a:
        if lista_itens==1:
            itens_selecionados.append(" Picanha : 25,90R$ ")
        elif lista_itens==2:
            itens_selecionados.append(" Lasanha : 20,90R$ ")
        elif lista_itens==3:
            itens_selecionados.append(" Strogonoff : 18,90R$ ")
        elif lista_itens==4:
            itens_selecionados.append(" Bife acebolado : 15,90R$ ")
        elif lista_itens==5:
            itens_selecionados.append(" Feijoada : 50,90R$ ") 
        elif lista_itens==6:
            itens_selecionados.append(" Macarronada : 19,90R$ ")
        elif lista_itens==7:
            itens_selecionados.append(" Bebidas : 5,90R$ ")
    return itens_selecionados

#Processando pagamento
def imprimindo_pagamento(a,b,c):
    total = a
    valor_total, desconto = b(opcao3,carrinho_de_compra)
    forma_pag=[]
    if c != 2:
        if c == 1:
            forma_pag.append('Débito')
        elif c == 3:
            forma_pag.append('Dinheiro')
        elif c== 4:
            forma_pag.append('Pix')
         
        for pag in forma_pag:
            print(f"\nPagamento: {pag}\n")
        print(f"Valor Bruto: {total:.2f}R$")
        print(f"Desconto: {desconto:.2f}R$")
        print(f"Total a pagar: {valor_total:.2f}R$")
    elif c == 2:
        forma_pag.append('Crédito')
        for pag in forma_pag:
            print(f"\nPagamento: {pag}\n")
        print(f"Valor Bruto: {total:.2f}R$")
        print(f"Acréscimo: {desconto:.2f}R$")
        print(f"Total a pagar: {valor_total:.2f}R$")

while True:
    cardapio_apresentacao()
    while True:
        opcao = int(input("Escolha seu prato: "))
        lista_selecao.append(opcao)
        if (opcao >=1)and(opcao <=7):
            break
        else:
            print("\nCodigo de prato invalido, informe o codigo do prato novamente.")
            time.sleep(2)
            os.system("cls||clear")
            cardapio_apresentacao()
    match(opcao):
        case 1:
            picanha=codigo_card(opcao)    
            carrinho_de_compra.append(picanha)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao 
            else:
                break
        case 2:
            lasanha=codigo_card(opcao)    
            carrinho_de_compra.append(lasanha)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==2:
                os.system("cls||clear")
                opcao
            else:
                break
        case 3:
            strogonoff=codigo_card(opcao)    
            carrinho_de_compra.append(strogonoff)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao
            else:
                break
        case 4:
            bife_acebolado=codigo_card(opcao)    
            carrinho_de_compra.append(bife_acebolado)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao
            else:
                break
        case 5:
            feijoada=codigo_card(opcao)    
            carrinho_de_compra.append(feijoada)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao
            else:
                break
        case 6:
            macarronada=codigo_card(opcao)    
            carrinho_de_compra.append(macarronada)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao
            else:
                break
        case 7:
            bebidas=codigo_card(opcao)    
            carrinho_de_compra.append(bebidas)
            opcao2=int(input("""Deseja adcionar outro prato ?
0- NÂO
1- SIM
        : """))
            if opcao2==1:
                os.system("cls||clear")
                opcao
            else:
                break

while True:
    opcao3 = int(input(""" \n==== PAGAMENTO ====\n
1- DEBITO
2- CRÉDITO
3- DINHEIRO
4- PIX
            : """)) 
    while True:
        if (opcao >=1) or (opcao <=4):
                break
        else:
            print("\nA opção selecionada está incorreta: ")
            time.sleep(2)
    match (opcao3):
        case 1 | 2 | 3 | 4:
            total = sum(carrinho_de_compra)
            imprimindo_pagamento(total,finalizando_compra,opcao3) 
            compra=pratos_selecionados(lista_selecao)
            print("\n=== PRATOS SELECIONADOS ===\n")
            for pratos in compra:
                print(pratos)          
            break