import numpy as np
import busca as bs
import math

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

    #print(result)

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

    #print(result)

    return result

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:
        result = True
    else:
        result = False

    #print(result)

    return result

def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi] or vi in listaAdj[vj]:
        #print(True)
        return True
    else:
        #print(False)
        return False
    
def caminhoEuleriano(matriz):
    matrizNp = np.array(matriz)
    n, s = matrizNp.shape
    total = 0
    i = 0

    while total <= 2 and i < n:
        grau = np.sum(matrizNp[i])
        if np.sum(matrizNp[i]) % 2 != 0:
            total += 1
        i += 1

    if total > 2:
        ret = False
    else:
        ret = True

    #print(ret)

    return ret

def classificaArestas(listaAdj, inicio = None):
    if inicio == None:
        inicio = 0

    tamLista = len(listaAdj)
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for i in range(tamLista)]
    tipoAresta = [[' ' for i in range(tamLista)] for j in range(tamLista)]
    tempoD = [0 for i in range(tamLista)]
    tempoT = [0 for i in range(tamLista)]
    ordenacaoTop = []

    bs.visitaDFS(inicio, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, True, ordenacaoTop)

    for vertice in listaAdj:
        if cor[vertice] == 'branco':
            bs.visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, True, ordenacaoTop)

    return tipoAresta

def temposVertices(listaAdj, inicio = None):
    if inicio == None:
        inicio = 0

    tamLista = len(listaAdj)
    listaTempo = {}
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for i in range(tamLista)]
    tipoAresta = [[' ' for i in range(tamLista)] for j in range(tamLista)]
    tempoD = [0 for i in range(tamLista)]
    tempoT = [0 for i in range(tamLista)]
    ordenacaoTop = []

    bs.visitaDFS(inicio, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, False, ordenacaoTop)

    for vertice in listaAdj:
        if cor[vertice] == 'branco':
            bs.visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, False, ordenacaoTop)

    for vertice in listaAdj:
        listaTempo[vertice] = str(tempoD[vertice]) + '/' + str(tempoT[vertice])

    print(listaTempo)

    return tempoD, tempoT

def verificaDAG(listaAdj):
    tamLista = len(listaAdj)
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for i in range(tamLista)]
    tipoAresta = [[' ' for i in range(tamLista)] for j in range(tamLista)]
    tempoD = [0 for i in range(tamLista)]
    tempoT = [0 for i in range(tamLista)]
    ordenacaoTop = []

    for vertice in listaAdj:
        if cor[vertice] == 'branco':
            bs.visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, False, ordenacaoTop)

    for linha in tipoAresta:
        if 'Back' in linha:
            return False

    return True

def ordenacaoTopologica(listaAdj):
    tamLista = len(listaAdj)
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for i in range(tamLista)]
    tipoAresta = [[' ' for i in range(tamLista)] for j in range(tamLista)]
    tempoD = [0 for i in range(tamLista)]
    tempoT = [0 for i in range(tamLista)]
    ordenacaoTop = []

    for vertice in listaAdj:
        if cor[vertice] == 'branco':
            bs.visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, False, ordenacaoTop)

    ordenacaoTop = ordenacaoTop[::-1]   #inverte

    return ordenacaoTop

def prim(matriz):
    numVertices = len(matriz)
    custoTotal = 0
    vertice = 0
    verSelec = []
    verNaoSelec = [i for i in range(1, numVertices)]
    arestasAGM = []

    verSelec.append(vertice)

    while len(arestasAGM) < numVertices - 1:
        custo = math.inf
        adj = None

        for u in verSelec:
            for v in verNaoSelec:
                if matriz[u][v] != 0 and matriz[u][v] < custo:
                    custo = matriz[u][v]
                    aresta = (u, v)

        verSelec.append(aresta[1])
        verNaoSelec.remove(aresta[1])
        arestasAGM.append(aresta)
        custoTotal += custo

    return arestasAGM, custoTotal

def kruskal(matriz):
    numVertices = len(matriz)
    custoTotal = 0
    listaArestas = []
    arestasAGM = []

    for i in range(numVertices):
        for j in range(i + 1, numVertices):
            if matriz[i][j] != 0:
                listaArestas.append((i, j, matriz[i][j]))

    listaArestas = sorted(listaArestas, key=lambda x: x[2])

    pai = [-1] * numVertices

    for aresta in listaArestas:
        raiz1 = find(pai, aresta[0])
        raiz2 = find(pai, aresta[1])

        if raiz1 != raiz2:
            arestasAGM.append((aresta[0], aresta[1]))
            union(pai, raiz1, raiz2)
            custoTotal += aresta[2]

    return arestasAGM, custoTotal

def find(pai, vertice):
    if pai[vertice] == -1:
        return vertice
    return find(pai, pai[vertice])

def union(pai, raiz1, raiz2):
    pai[raiz2] = raiz1
