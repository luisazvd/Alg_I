'''

import math

def somar(a, b):
    soma = a + b
    print(a, "+", b, "=", soma)


def multiplicar(x, y):
    mult = x * y
    print(x, "X", y, "=", mult)


def raiz(r):
    raiz = math.sqrt(r)
    print("A raiz quadrada de", r, "é:", raiz)


def potencia(j, k):
    pot = j ** k
    print(j, "^", k, "=", pot)


def tabuada(g):
    for i in range(0, 11):
        tab = g * i
        print(g, "x", i, "=", tab)

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
'''
import random
import funcoes

tam = int(input("Informe o tamanho:"))
v = funcoes.criarVetor(tam)

funcoes.exibirVetor(v)

s1 = funcoes.somaImpares(v)
print("Soma dos ímpares do vetor:", s1)

num = int(input("Informe o número para ser buscado:"))
funcoes.busca(num, v)

ordena = int(input("Informe a forma de ordenação:"))
v = funcoes.ordenar(ordena, v)
funcoes.exibirVetor(v)
