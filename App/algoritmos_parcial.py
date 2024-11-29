#dfs normal
def dfs_vertex(search, graph, vertex):
    """
    Algoritmo recursivo DFS a partir del vértice `vertex`.
    La solución de los vértices alcanzables queda en la estructura `search`.

    Params:
    - search: estructura con el resultado de los vértices alcanzados desde el vértice source.
    - graph: grafo a recorrer.
    - vertex: vértice a explorar.

    Returns:
    - La estructura `search` actualizada.
    """
    for w in graph[vertex]:
        if w not in search['visited']:
            search['visited'].add(w)
            search['edges'].setdefault(vertex, []).append(w)
            dfs_vertex(search, graph, w)
    return search

#dfo 
def dfs_vertex(graph, search, vertex):
    """
    Aplicar el algoritmo DFS desde `vertex` actualizando los recorridos `pre`, `post`, y `reversepost`.

    Returns:
    - La estructura `search` actualizada.
    """
    search['pre'].append(vertex)
    search['marked'][vertex] = True

    for v in graph[vertex]:
        if not search['marked'].get(v, False):
            dfs_vertex(graph, search, v)
    
    search['post'].append(vertex)
    search['reversepost'].append(vertex)
    return search

#bfs
def bfs_vertex(search, graph, source):
    """
    Algoritmo iterativo BFS a partir del vértice `source`.
    La solución de los vértices alcanzables queda en la estructura `search`.

    Returns:
    - La estructura `search` actualizada.
    """
    queue = deque([source])
    search['visited'].add(source)

    while queue:
        vertex = queue.popleft()
        for w in graph[vertex]:
            if w not in search['visited']:
                queue.append(w)
                search['visited'].add(w)
                search['edges'].setdefault(vertex, []).append(w)
    return search
#de clase
def bfs_vertex(search, graph, source):
    cola = q.new_queue()
    q.enqueue(cola, source)
    while not q.is_empty(cola):
        vertex = q.dequeue(cola)
        lst_ady = mapa.get(graph["vertices"], vertex)
        for i in range(t.size(lst_ady)):
            arco = t.get_element(lst_ady, i)
            W = e.other(arco, vertex)
            marca = mapa.get(search["visited"], W)
            if marca is None:
                q.enqueue(cola, W)
                mapa.put(search["visited"], W, {
                    "marked": True,
                    "edge_to": vertex,
                    "dist_to": distancia
                })
    if marca is None:
        q.enqueue(cola, W)
        mapa.put(search["visited"], W, {
            "marked": True,
            "edge_to": vertex,
            "dist_to": distancia
    })

    marca_vertex = mapa.get(search["visited"], vertex)
    dist_to_vertex = marca_vertex["dist_to"]
