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

    #print(analisado)

    return analisado

def DFSr(listaAdj, inicio):
    analisado = []

    DFS_recursivo(listaAdj, inicio, analisado)

    print(analisado)

def DFS_recursivo(listaAdj, inicio, analisado):
    analisado.append(inicio)
    
    for adj in listaAdj[inicio]:
        if adj not in analisado:
            DFS_recursivo(listaAdj, adj, analisado)

def DFS(listaAdj, inicio):
    analisado = []
    cont = -1

    while len(analisado) < len(listaAdj):
        if inicio not in analisado:
            analisado.append(inicio)
        
        for i in range(len(listaAdj)):
            if i in listaAdj[inicio] and i not in analisado:
                inicio = i
                analisado.append(i)
                break
            elif i == len(listaAdj) - 1:
                cont += 1
                inicio = cont

    #print(analisado)

    return analisado
