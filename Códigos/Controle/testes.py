import numpy as np

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

    listaTempo = {}
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for i in range(len(listaAdj))]
    tipoAresta = [[' ' for i in range(len(listaAdj))] for j in range(len(listaAdj))]
    tempoD = [0 for i in range(len(listaAdj))]
    tempoT = [0 for i in range(len(listaAdj))]

    for vertice in listaAdj:
        if cor[vertice] == 'branco':
            visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo)

    for vertice in listaAdj:
        listaTempo[vertice] = str(tempoD[vertice]) + '/' + str(tempoT[vertice])

    print(listaTempo)

    return tipoAresta

def visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo):
    cor[vertice] = 'cinza'
    tempo[0] += 1
    tempoD[vertice] = tempo[0]

    for adj in listaAdj[vertice]:
        if cor[adj] == 'branco':
            tipoAresta[vertice][adj] = 'Tree'
            print(vertice, adj, 'Tree')
            visitaDFS(adj, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo)
        elif cor[adj] == 'cinza':
            tipoAresta[vertice][adj] = 'Back'
            print(vertice, adj, 'Back')
        else:
            if tempoD[vertice] < tempoD[adj]:
                tipoAresta[vertice][adj] = 'Forward'
                print(vertice, adj, 'Forward')
            else:
                tipoAresta[vertice][adj] = 'Cross'
                print(vertice, adj, 'Cross')
    
    cor[vertice] = 'preto'
    tempo[0] += 1
    tempoT[vertice] = tempo[0]
