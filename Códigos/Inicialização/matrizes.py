import numpy as np

def criarMatrizArquivo(instancia):
    with open('C:/Users/rocha/Documents/Unifei/Algoritmos em Grafos/Grafos/Instâncias/' + instancia + '.txt', 'rb') as f:
        matriz = np.genfromtxt(f, dtype="int64") #Leitura do arquivo e armazenamento em uma matriz numpy
    return matriz

def criaListaAdjacencias(matriz1):
    matriz = np.array(matriz1)
    linha, coluna = matriz.shape
    listaAdj = {}

    for i in range(linha):
        listaAdj[i] = []
        for j in range(coluna):
            num = matriz[i][j]
            while(num>0):   #se houverem mais arestas, o vértice será repetido
                listaAdj[i].append(j)
                num -= 1

    return listaAdj

def warshall(matriz):
    matrizAlc = np.array(matriz)
    n, s = matrizAlc.shape

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrizAlc[i][j] == 1 or (matrizAlc[i][k] == 1 and matrizAlc[k][j] == 1):
                    matrizAlc[i][j] = 1
                else:
                    matrizAlc[i][j] = matrizAlc[i][j]

    return matrizAlc
