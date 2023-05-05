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
    tamanhoLista = len(listaAdj)
    cont = -1

    while len(analisado) < tamanhoLista:    #deve analisar todos os vértices
        if inicio not in analisado: #marca o vértice como analisado caso não tenha sido marcado ainda
            analisado.append(inicio)
        
        for i in range(tamanhoLista):   #varre todos os valores possíveis para serem adjacentes de um vértice
            if i in listaAdj[inicio] and i not in analisado:    #o número é adjacente e não foi analisado
                inicio = i  #pula para o próximo vértice
                analisado.append(i)
                break
            elif i == tamanhoLista - 1: #caso seja o último elemento possível e nada foi feito ainda
                cont += 1
                inicio = cont   #pula para o próximo vértice, começando do 0

    return analisado
