def Floyd (graph) :
    inf = 1000
    n = len(graph)
    
    D = [[inf] * n for _ in range(n)]
    P = [[-1] * n for _ in range(n)]

    for i in range (n) :
        for j in range (n) :
            D[i][j] = graph[i][j]
            if (i != j) and (graph[i][j] != inf) : P[i][j] = j

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if (D[i][j] > D[i][k] + D[k][j]) :
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[i][k]

    return D, P

def print_path (P, s, e) :
    s -= 1 # start vertex
    e -= 1 # end vertex
    
    path = [s]
    
    while (P[path[-1]][e] != -1) :
        path.append(P[path[-1]][e])

    for i in range (len(path)) :
        path[i] += 1

    print(f" v{s+1} -> v{e+1} :: {' -> '.join(map(str, path)) }")

if (__name__ == "__main__") :
    inf = 1000
    graph = [[0, 4, inf, inf, 4], [6, 0, inf, inf, inf], [1, 2, 0, 1, inf], [inf, inf, 4, 0, inf], [9, inf, 3, 5, 0]]
    d, p = Floyd(graph)

    print_path(p, 1, 2)
    print_path(p, 1, 3)
    print_path(p, 1, 4)
    print_path(p, 1, 5) 
