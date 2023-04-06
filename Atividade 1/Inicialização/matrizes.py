import numpy as np

def criarMatrizArquivo(instancia):
    with open('C:/Users/rocha/Documents/Unifei/Algoritmos em Grafos/Atividade 1/Instâncias/' + instancia + '.txt', 'rb') as f:
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

    #print(listaAdj)

    return listaAdj
