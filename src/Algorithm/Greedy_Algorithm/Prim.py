def Prim (W : list) -> list :
    '''
    '''
    inf = 1000

    n = len(w)
    F = set()
    nearest = [0] * n
    distance = [0] * n
    
    for i in range (1, n) :
        nearest[i] = 0
        distance[i] = w[0][i]

    for i in range (n-1) :
        m = inf
        vnear = 0
        
        for j in range (1, n) :
            if (0 < distance[j] < m) :
                m = distance[j]
                vnear = j
        F.add((vnear, nearest[vnear]))
                
        distance[vnear] = -1
        
        for j in range (1, n) :
            if (w[vnear][j] < distance[j]) :
                distance[j] = w[vnear][j]
                nearest[j] = vnear

    return F
    

if (__name__ == "__main__") :
    inf = 1000
    w = [[0, 1, 3, inf, inf], [1, 0, 3, 6, inf], [3, 3, 0, 4, 2], [inf, 6, 4, 0, 5], [inf, inf, 2, 5, 0]]
    print(Prim (w))
    
