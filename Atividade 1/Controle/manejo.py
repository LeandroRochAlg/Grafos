import numpy as np

def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1

    print(matriz)
    
    return matriz

def insereArestaLista(lista, vi, vj):
    lista[vi].append(vj)
    lista[vi].sort()

    lista[vj].append(vi)
    lista[vj].sort()

    print(lista)

    return lista

def insereVertice(matriz):
    tam = len(matriz)
    
    zeros = [0] * (tam)

    matriz.append(zeros)

    for linha in matriz:
        linha.append(0)

    matrizNp = np.array(matriz)

    print(matrizNp)
    
    return matrizNp

def insereVerticeLista(lista):
    for i in lista:
        if i == len(lista)-1:
            lista[i+1] = []
            break

    print(lista)

    return lista

def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0

    print(matriz)
    
    return matriz

def removeArestaLista(lista, vi, vj):
    listaVi = lista[vi]
    listaVj = lista[vj]

    for i in range(len(lista[vi])):
        if listaVi[i] == vj:
            lista[vi].pop(i)
            break

    for j in range(len(lista[vj])):
        if listaVj[j] == vi:
            lista[vj].pop(j)
            break


    print(lista)

    return lista

def removeVertice(matriz, v):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j == v) or (i == v):
                matriz[i][j] = -1

    matrizNp = np.array(matriz)

    print(matrizNp)
    
    return matrizNp

def removeVerticeLista(lista, v):
    del lista[v]

    for j in lista:
        listaV = lista[j]
        for i in range(len(listaV)):
            if listaV[i] == v:
                while i<len(listaV) and listaV[i] == v:
                    lista[j].pop(i)
                break

    print(lista)

    return lista
