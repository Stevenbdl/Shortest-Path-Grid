import networkx as nx 


G = nx.Graph()#Grafo


def gridElementToString(grid):
    """
    Crea un nuevo arreglo y agrega todos los elementos del grid pasado por parametro convertidos a string
    esto se hace para que puedan utilizarse como nodos y vertices de un grafo
    """
    newgrid = []#nuevo grid
    for r in grid:#Fila en el grid
        row = []
        for c in r:
            row.append(str(c))
        newgrid.append(row)
        row = []#Limpiar o vaciar la fila ya agregada al nuevo grid

    return newgrid

def dijkstra(grid, graph, start, end, walls):
    """
    grid -> list[[str]]
    graph -> nx.Graph
    start -> [x, y]
    end -> [x, y]
    walls -> [x, y]
    """
    for node_r, row in enumerate(grid):
        for node_c, column in enumerate(row):
            #**********************************Agrega nodos arriba y abajo**************************************************
            # si la fila actual está entre el rango de 
            if node_r in range(1, len(grid) - 1):
                graph.add_edge(column, grid[node_r-1][node_c])#Agrega el elemento que le quede arriba [x, y-1]
                graph.add_edge(column, grid[node_r+1][node_c])#Agrega el elemento que le quede abajo [x, y+1]
            else:# determinar en cual fila está si es en la primera o en la última fila del grid
                #si la fila actual es la primera solo enlaza el nodo de abajo ya que no tendría nodo arriba
                if node_r == 0:
                    graph.add_edge(column, grid[node_r+1][node_c])#Agrega el elemento que le quede abajo [x, y+1]
                #Si la fila es la última está solo enlaza el nodo de arriba ya que no tendría nodo abajo 
                elif node_r == len(grid) - 1:
                    graph.add_edge(column, grid[node_r-1][node_c])#Agrega el elemento que le quede arriba [x, y-1]
            
            #***********************************Agrega nodos izquierda derecha*********************************************
            #Si el elemento en la fila no está ni al comienzo ni al final de la lista agregar nodos de izquierda a derecha
            if node_c in range(1, len(row) - 1):
                graph.add_edge(column, grid[node_r][node_c - 1])#Agrega el elemento que le queda a la izquierda [x-1, y]
                graph.add_edge(column, grid[node_r][node_c + 1])#Agrega el elemento que le queda a la derecha [x+1, y]
            else:#si el nodo está al comienzo de la fila o al final
                #si el nodo está al comienzo de la fila pues solo agregar el nodo que le queda a la derecha
                if node_c == 0:
                    graph.add_edge(column, grid[node_r][node_c + 1])#Agrega el elemento que le queda a la derecha [x+1, y]
                elif node_c == len(row) - 1:
                    graph.add_edge(column, grid[node_r][node_c - 1])#Agrega el elemento que le queda a la izquierda [x-1, y]

    
    #remover los nodos que son muros en el grid
    for w in walls:
        if w in graph:
            graph.remove_node(w)
   
    return nx.shortest_path(G, start, end)

