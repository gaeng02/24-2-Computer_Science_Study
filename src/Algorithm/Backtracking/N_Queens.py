def promising (i : int, col : list) :
    k = 0
    switch = True
    while ((k < i) and switch) :
        if ((col[i] == col[k]) or (abs(col[i] - col[k]) == i - k)) :
            switch = False
        k += 1
    return switch

def queens (n : int, i : int, col : list, cnt : int, cols : list, nodes : int) :
    if (promising(i, col)) :
        if (i == n - 1) :
            cnt += 1
            cols.append(col.copy())
        else :
            for j in range (n) :
                nodes += 1
                col[i + 1] = j
                cnt, cols, nodes = queens(n, i+1, col, cnt, cols, nodes)
    return cnt, cols, nodes

if (__name__ == "__main__") :

    n = 4       # 바둑판의 사이즈. Square 
    
    cnt, cols, nodes = queens(n, -1, [0] * n, 0, [], 0)

    print(f" The number of solutions :: {cnt}")         # 해의 갯수
    print(f" Solution :: {cols}")                           # 경우의 수
    print(f" The total number of nodes :: {nodes}")     # 상태공간노드의 수 
    
