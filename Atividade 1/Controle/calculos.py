import numpy as np
from Inicialização import matrizes as mt
from Controle import testes as ts

def calcDensidadeLista(listaAdj):
    numV = 0
    numE = 0

    for i in listaAdj:
        numV += 1
        for j in listaAdj[i]:
            listaAdj[j].pop(0)  #não conta a mesma aresta duas vezes
            numE += 1

    if ts.tipoGrafoLista(listaAdj) % 10 > 0:   #Digrafo
        densidade = (numE)/(numV*(numV - 1))
    else:
        densidade = (2*numE)/(numV*(numV - 1))

    print(round(densidade, 3))
    return densidade
