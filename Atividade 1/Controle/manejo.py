import numpy as np

def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1

    print(matriz)
    return matriz

def insereVertice(matriz):
    tam = len(matriz)
    
    zeros = [0] * (tam)

    matriz.append(zeros)

    for linha in matriz:
        linha.append(0)

    matrizNp = np.array(matriz)

    print(matrizNp)
    return matrizNp

def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0

    print(matriz)
    return matriz

def removeVertice(matriz, v):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j == v) or (i == v):
                matriz[i][j] = -1

    matrizNp = np.array(matriz)

    print(matrizNp)
    return matrizNp