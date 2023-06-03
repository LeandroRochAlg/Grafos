import math

def BFS(listaAdj, inicio):
    Q = []
    analisado = []

    Q.append(inicio)

    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)

        for j in listaAdj[v]:
            if j not in analisado:
                Q.append(j)
        
        if v not in analisado:
            analisado.append(v)

    for i in listaAdj:
        if len(listaAdj[i]) == 0:
            analisado.append(i)
            
    return analisado

def DFSr(listaAdj, inicio):
    analisado = []

    DFS_recursivo(listaAdj, inicio, analisado)
    
    return analisado

def DFS_recursivo(listaAdj, inicio, analisado):
    analisado.append(inicio)
    
    for adj in listaAdj[inicio]:
        if adj not in analisado:
            DFS_recursivo(listaAdj, adj, analisado)

def DFSi(listaAdj, inicio):
    analisado = []
    aux = []    #pilha de vértices
    tamanhoLista = len(listaAdj)
    conti = 0
    cont = 0

    aux.append(inicio)

    while len(analisado) < tamanhoLista:    #deve analisar todos os vértices
        while len(aux) - conti >= 0:
            if inicio not in analisado: #marca o vértice como analisado caso não tenha sido marcado ainda
                analisado.append(inicio)

            for i in range(tamanhoLista):   #varre todos os valores possíveis para serem adjacentes de um vértice
                if i in listaAdj[inicio] and i not in analisado:    #o número é adjacente e não foi analisado
                    inicio = i  #pula para o próximo vértice
                    analisado.append(i)
                    aux.append(i)
                    conti = 0
                    break
                elif i == tamanhoLista - 1: #caso seja o último elemento possível e nada foi feito ainda
                    conti += 1
                    if len(aux) - conti >= 0:
                        inicio = aux[len(aux) - conti]

        inicio = cont
        cont += 1    #reinicia o contador da pilha

    return analisado

def visitaDFS(vertice, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, classifica, ordenacaoTop):
    cor[vertice] = 'cinza'
    tempo[0] += 1
    tempoD[vertice] = tempo[0]

    for adj in listaAdj[vertice]:
        if cor[adj] == 'branco':
            tipoAresta[vertice][adj] = 'Tree'
            if classifica:
                print(vertice, adj, 'Tree')
            visitaDFS(adj, listaAdj, cor, tipoAresta, tempoD, tempoT, tempo, classifica, ordenacaoTop)
        elif cor[adj] == 'cinza':
            tipoAresta[vertice][adj] = 'Back'
            if classifica:
                print(vertice, adj, 'Back')
        else:
            if tempoD[vertice] < tempoD[adj]:
                tipoAresta[vertice][adj] = 'Forward'
                if classifica:
                    print(vertice, adj, 'Forward')
            else:
                tipoAresta[vertice][adj] = 'Cross'
                if classifica:
                    print(vertice, adj, 'Cross')
    
    cor[vertice] = 'preto'
    tempo[0] += 1
    tempoT[vertice] = tempo[0]
    ordenacaoTop.append(vertice)

def dijkstra(matriz, vOrigem, vDestino):
    num_vertices = len(matriz)
    custo = [math.inf] * num_vertices
    rota = [-1] * num_vertices
    custo[vOrigem] = 0

    verAbertos = set(range(num_vertices))
    verFechados = set()

    while verAbertos:
        v = min(verAbertos, key=lambda x: custo[x])
        verAbertos.remove(v)
        verFechados.add(v)

        if v == vDestino:
            break

        for j in range(num_vertices):
            if j not in verFechados and matriz[v][j] != -1:
                aresta = matriz[v][j]
                dist = custo[v] + aresta
                if dist < custo[j]:
                    custo[j] = dist
                    rota[j] = v

    caminho = []
    atual = vDestino
    while atual != -1:
        caminho.insert(0, atual)
        atual = rota[atual]

    custo_rota = custo[vDestino]

    return caminho, custo_rota
