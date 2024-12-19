from os import system

#Coletando dados:
system("cls||clear")
nome = str(input("Nome do jogador")) #Utilizando o STR para obter os dados em formato de texto
gols = str(input("Numero de gols"))

def funcao(nome='<Desconhecido>', gols = 0):
    print(f"O Jogador {nome} fez {gols} gol(s) no campeonato")

if gols.isnumeric():
    gols = int(gols)#Convertendo o texto em numeros caso o texto seja apenas numerico, utilizando parametros
else:
    gols = 0
if nome.strip() == '':#Retirando todos os espaços do  texto geado em nome
    funcao(gols=gols)
else:
    funcao(nome,gols)

