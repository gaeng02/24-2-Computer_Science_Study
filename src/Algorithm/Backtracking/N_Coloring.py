def promising (i, vcolor, graph) :
    j = 0
    switch = True
    while ((j < i) and (switch)) :
        if (graph[i][j] and (vcolor[i] == vcolor[j])) : switch = False
        j += 1
    return switch

def m_coloring (i, vcolor, graph, m, solutions, nodes) :
    nodes += 1
    if promising(i, vcolor, graph) :
        if (i == len(vcolor) - 1) : solutions.append(vcolor.copy())
        else :
            for color in range (m) :
                vcolor[i + 1] = color + 1
                solutions, nodes = m_coloring(i + 1, vcolor, graph, m, solutions, nodes)

    return solutions, nodes

if (__name__ == "__main__") :

    m = 2
    W = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]

    n = len(W)
    vcolor = [0] * n

    solutions, nodes = m_coloring(-1, vcolor, W, m, [], 0)

    print(f" Graph :: ")
    for row in W : print(f" {row}")

    print(f" The number of solutions :: {len(solutions)}")
    for solution in solutions : print(f" {solution}")
    print(" The total number of nodes ::", nodes)

