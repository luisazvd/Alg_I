'''
# PARTE 1

Criar função chamada criarVetor que recebe um número inteiro por parâmetro representando o tamanho de um vetor. 
A função deve criar o vetor, preencher com valores aleatórios entre 1 e 200 e retornar o vetor.
No algoritmo principal, solicite o tamanho do vetor para o usuário e crie o vetor utilizando a função.

# PARTE 2

Crie um procedimento chamado exibirVetor para exiba na tela o vetor recebido por parâmetro.

# PARTE 3

Crie uma função chamada somaImpares que calcule e retorne a soma de todos os números ímpares de um vetor recebido por parâmetro.
No algoritmo principal, apresente a soma na tela.

# PARTE 4

Implemente um procedimento chamado busca que recebe por parâmetro um número informado pelo usuário. O procedimento deve, usando a busca sequencial, exibir uma mensagem na tela dizendo se o número está ou não presente em um vetor também recebido por parâmetro.

# PARTE 5

Implemente uma função chamada ordenar que recebe dois parâmetros: um vetor de números inteiros e o nome de um algoritmo de ordenação(bolha, inserção ou seleção).
Ordene e retorne o vetor recebido de acordo com o parâmetro de ordenação. Obs: o código de ordenação está no Moodle(tópico Aulas)
No algoritmo principal, utilize o procedimento exibirVetor para mostrar o vetor ordenado.

'''

import random


def criarVetor(a):  # 1
    vetor = [0] * a
    for i in range(0, len(vetor)):
        vetor[i] = random.randint(0, 200)

    return vetor


def exibirVetor(b):  # 2
    print("Vetor:", end= "")
    for i in range(0, len(b)):
        print(b[i], end= " ")
    print(" ")

def somaImpares(c):  # 3
    soma = 0
    for i in range(0, len(c)):
        if (c[i] % 2 != 0):
            soma += c[i]
    return soma


def busca(valor, d):  # 4
    iValor = -1
    for i in range(0, len(d)):
        if(d[i] == valor):
            iValor = i
            break
    if(iValor == True):
        print("O", valor, "está no vetor na posição", iValor)
    else:
        print("O", valor, "não está no vetor")


def ordenar(tipo, vetor):
    if(tipo == 1):  # bolha
        for i in range(len(vetor)-1, 0, -1):
            for j in range(0, i):
                if (vetor[j] > vetor[j+1]):
                    aux = vetor[j+1]
                    vetor[j+1] = vetor[j]
                    vetor[j] = aux

    elif(tipo == 2):  # inserção
        for i in range(0, len(vetor)-1):
            menor = vetor[i]
            pmenor = i
            for j in range(i+1, len(vetor)):
                if(menor > vetor[j]):
                    menor = vetor[j]
                    pmenor = j
            c = vetor[i]
            vetor[i] = menor
            vetor[pmenor] = c

    elif(tipo == 3):  # seleção
        for i in range(1, len(vetor)):
            valor = vetor[i]
            j = i - 1
            while(j >= 0 and vetor[j] > valor):
                vetor[j+1] = vetor[j]
                j -= 1
            vetor[j+1] = valor
    else:
        print("Forma de ordenação invalida")
    return vetor
