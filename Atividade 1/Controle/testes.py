import numpy as np
from Inicialização import matrizes as mt

def tipoGrafo(matriz1):
    flagS = 0
    flagM = 0
    flagP = 0

    matriz = np.array(matriz1)
    linha, coluna = matriz.shape

    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] > 1:    #Multigrafo
                flagM = 20
            if i == j and matriz[i][j] > 0:    #Pseudografo
                flagP = 30
            if matriz[i][j] != matriz[j][i]:    #Digrafo
                flagS = 1

    if flagP != 0:
        result = flagP + flagS
    else:
        result = flagM + flagS

    print(result)

    return result

def tipoGrafoLista(listaAdj):
    flagS = 0
    flagM = 0
    flagP = 0

    #Simples ou digrafo:
    for i in listaAdj:
        k = -1
        for j in listaAdj[i]:
            if (i not in listaAdj[j]):  #Digrafo
                flagS = 1
            if k == j: #Multigrafo
                flagM = 20
            if j == i:  #Pseudografo
                flagP = 30
            k = j

    if flagP != 0:
        result = flagP + flagS
    else:
        result = flagM + flagS

    print(result)

    return result

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:
        result = True
    else:
        result = False

    print(result)

    return result

def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi] or vi in listaAdj[vj]:
        print(True)
        return True
    else:
        print(False)
        return False
