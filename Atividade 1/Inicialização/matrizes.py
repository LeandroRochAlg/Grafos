import numpy as np

def criarMatrizArquivo(instancia):
    with open('C:/Users/rocha/Documents/Unifei/Algoritmos em Grafos/Atividade 1/Instâncias/' + instancia + '.txt', 'rb') as f:
        matriz = np.genfromtxt(f, dtype="int64") #Leitura do arquivo e armazenamento em uma matriz numpy
    return matriz