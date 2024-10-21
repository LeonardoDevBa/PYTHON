from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from os import system
from time import sleep
from dataclasses import dataclass

BD = create_engine("sqlite:///bancodedados.db")

Session = sessionmaker(bind=BD)
session = Session()

Base = declarative_base()

@dataclass
class Trabalhador(Base):
    __tablename__ = "trabalhadores"
    
    nome = Column(String)
    sobrenome = Column(String)
    cpf = Column(String, primary_key=True)
    salario = Column(Float)
    dependente = Column(Integer)
    senha = Column(String)

Base.metadata.create_all(BD)

def verificando_cpf():
    while True:
        cpf = input("Informe seu CPF: ") 
        id_usuario = session.query(Trabalhador).filter(Trabalhador.cpf == cpf).first()
        if id_usuario is None:  
            break
        else:
            print("CPF já cadastrado")
    
    return cpf

def cadastro():
    cpf = verificando_cpf()
    
    funcionario = Trabalhador(
        nome=input("Insira um nome: "),
        sobrenome=input("Insira um sobrenome: "),
        cpf=cpf,
        salario=float(input("Insira o salário bruto: ")),
        dependente=int(input("Informe a quantidade de dependentes: ")),
        senha=input("Crie uma senha: ")
    )
    session.add(funcionario)
    session.commit()

def menu():
    print("=" * 20)
    print("""
1- ADICIONAR FUNCIONARIO
2- CALCULO SALARIAL""")
    print("=" * 20)

def desconto_inss(salario):
    if salario <= 1100:
        desconto = salario * 0.075
    elif salario <= 2203.48:
        desconto = salario * 0.09
    elif salario <= 3305.22:
        desconto = salario * 0.12
    elif salario <= 6433.57:
        desconto = salario * 0.14
    else:
        desconto = 854.36
    return desconto

def beneficios (salario,dependente):
    print("="*40)
    print(f"{"BENEFICIOS":^40}")
    print("="*40)

    opcao10 = int(input("Você deseja receber vale transporte ? \n1-Sim \n2-Não"))
    beneficio = float(input("Informe o valor do Ticket alimentação: "))
    if opcao10 == 1:
        transporte = (salario*0.06)
    else:
        transporte = 0
    refeicao = (beneficio*0.2)
    plano_saude = (150*dependente)
    return transporte, refeicao, plano_saude

def imposto_de_renda(salario1, inss, dependentes):
    deducao = dependentes * 189
    base_ir = salario1 - inss - deducao
    if base_ir <= 2259.20:       
        desconto = 0
    elif base_ir <= 2826.65:
        desconto = (base_ir * 0.075) - 142.80    
    elif base_ir <= 3751.05:
        desconto = (base_ir * 0.15) - 354.80        
    elif base_ir <= 4664.68:
        desconto = (base_ir * 0.225) - 636.13
    else:
        desconto = (base_ir * 0.275) - 869.
    return desconto

while True:
    system("cls||clear")
    menu()
    opcao = int(input("Informe a opão desejada: "))
    if opcao == 1:
        while True:
            cadastro()
            opcao1 = int(input("Deseja adicionar outro funcionario ? \n1-SIM \n2-NÃO"))
            if opcao1 == 2:
                break
    elif opcao == 2:
        system("cls||clear")
        print("="*40)
        print(f"{"LOGIN":^40}")
        print("="*40)
        cpf_login = input("Informe seu CPF para login: ")
        usuario = session.query(Trabalhador).filter(Trabalhador.cpf == cpf_login).first()
        senha_login = input("Informe senha: ")
        if usuario.senha == senha_login:
            print("="*40)
            print(f"Nome: {usuario.nome} {usuario.sobrenome}")
            print(f"CPF: {usuario.cpf}")
            print(f"Salario Bruto: {usuario.salario}")
            inss = desconto_inss(usuario.salario)
            desconto= imposto_de_renda(usuario.salario,inss, usuario.dependente)
            transporte, refeicao, plano_saude = beneficios(usuario.salario, usuario.dependente)
            print(f"Desconto INSS: {inss}")
            print(f"Desconto Imposto de renda: {desconto}")
            print(f"Vale transporte: {transporte}")
            print(f"Vale Refeição: {refeicao}")
            print(f"Plano de Saude: {plano_saude}")
            print(f"Salario liquido: {usuario.salario - transporte - refeicao - plano_saude - desconto - inss} R$")
            sleep(20)
    else:
        print("Opção invalida:")
        sleep(2)
        system("cls||clear")