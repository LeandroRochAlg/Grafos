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

    while len(analisado) < tamanhoLista:
        if inicio not in analisado:
            analisado.append(inicio)
        
        for i in range(tamanhoLista):
            if i in listaAdj[inicio] and i not in analisado:
                inicio = i
                analisado.append(i)
                break
            elif i == tamanhoLista - 1:
                cont += 1
                inicio = cont

    return analisado
