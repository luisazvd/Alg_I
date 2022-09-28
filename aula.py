
'''
Variável local: identifica apenas em subalgoritmos 
Variável global: no algoritmo principal


def mostrarX():
    global x #referência para acessar a variável local por fora
    x = 20 #variável local



x = 10 #variável global
print(x)
mostrarX()
print(x)


def fatorial(num):
    fat = 1
    i = 1
    while (i <= num):
        fat = fat * i
        i += 1
    
    return fat #indica que o algoritmo tem um valor, ou seja, uma função e não procedimento 


x = int(input("Informe o número que deseja calcular o fatorial: !"))
print("Resultado:", fatorial(x))
'''

#1
import math

def somar(a, b):
    soma = a + b
    print(a,"+",b,"=",soma)

def multiplicar(x, y):
    mult = x * y
    print(x,"X",y,"=",mult)

def raiz(r):
    raiz = math.sqrt(r)
    print("A raiz quadrada de", r, "é:", raiz)

def potencia(j, k):
    pot = j ** k
    print(j,"^",k,"=",pot)

def tabuada(g):
    for i in range(0,11):
        tab = g * i
        print(g,"x",i,"=",tab)


opcao = 0
while(opcao != 6):
    print("=== MENU DE OPÇÕES ===")
    print("1. Somar 2 números")
    print("2. Multiplicar 2 números")
    print("3. Raiz quadrada de um número")
    print("4. Potência entre base e expoente")
    print("5. Tabudada de 1 a 10 de um número")
    print("6. Sair")
    print("Opção", end="")
    opc = int(input(":"))

    if(opc == 1):
        n1 = int(input("Informe o primeiro número:"))
        n2 = int(input("Informe o segundo número:"))
        somar(n1, n2)

    elif(opc == 2):
        n1 = int(input("Informe o primeiro número:"))
        n2 = int(input("Informe o segundo número:"))
        multiplicar(n1, n2)

    elif(opc == 3):
        n = int(input("Informe o número:"))
        raiz(n)
    
    elif(opc == 4):
        n1 = int(input("Informe a base:"))
        n2 = int(input("Informe o expoente:"))
        potencia(n1, n2)

    elif(opc == 5):
        n = int(input("Informe o número:"))
        tabuada(n)

    elif(opc == 6):
        print("Saindo..")
        break
    
    else:
        print("Número inválido!!!!")















  
