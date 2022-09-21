'''#1 - Imports

#2 - Sub-algoritmos
def exibirMensagem():
    print("Olá pessoal, tudo bem?")

#3 - Algoritmo principal
exibirMensagem()'''

import random
import math
import os

def limpar():
    input("")
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def somar():
    x = int(input("Primeiro valor:"))
    y = int(input("Segundo valor:"))
    z = int(input("Terceiro valor:"))
    soma = x + y + z
    print("A soma de tais valores é:", soma)

def raiz():
    r = int(input("Informe um número:"))
    raiz = math.sqrt(r)
    print("A raiz quadrada de",r, "é:", raiz)

def sorte():
    s = random.randint(0,100)
    print("O número sorteado foi:", s)

opcao = 0

while(opcao != 4 ):
    print("=== MENU DE OPÇÕES ===")
    print("1. Somar 3 números")
    print("2. Raiz quadrada de um número")
    print("3. Sortear um número de 0 a 100")
    print("4. Sair")
    print("Opção", end="")

    opc = int(input(":"))

    if(opc == 1):
        somar()
    
    elif(opc == 2):
        raiz()

    elif(opc == 3):
        sorte()
    
    elif(opc == 4):
        print("Saindo..")
        break
    else:
        print("Número inválido!!!!")
