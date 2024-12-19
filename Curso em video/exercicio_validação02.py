from os import system 
system("cls||clear")
branco = "\033[37m"
def leia(n:str):
    vermelho = "\033[31m"
    if n.isnumeric():
        n = int(n)
        return n    
    else:
        result = f"{vermelho}inválido"
        return result
    
#Solicitação de dados e validando eles:
while True:
    n = leia(n=str(input(f"{branco}Informe um numero: ")))
    print(f"O numero informado foi {n}")


    