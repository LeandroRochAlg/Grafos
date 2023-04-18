import numpy as np
from Inicialização import matrizes as mt

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

def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi] or vi in listaAdj[vj]:
        print(True)
        return True
    else:
        print(False)
        return False
