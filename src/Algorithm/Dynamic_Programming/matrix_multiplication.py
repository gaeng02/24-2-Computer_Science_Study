def print_matrix (matrix : list) :
    for i in matrix :
        for j in i :
            print(f'{j:4d}', end=" ")
        print()
    print()

def order (P : list, i : int, j : int) :
    if (i == j) :
        print(f"A{i}", end = "")
        
    elif (i < j) :
        k = P[i][j]
        print("(", end = "")
        
        order(P, i, k)
        print(end = "")

        order(P, k + 1, j)
        print(")", end = "")

def chain_multiplication (d : list) :
    n = len(data) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    p = [[0] * (n + 1) for _ in range(n + 1)]

    for diagonal in range (1, n) :
        for i in range(1, n - diagonal + 1) :
            j = i + diagonal
            m[i][j] = 999999
            for k in range (i, j) :
                v = m[i][k] + m[k+1][j] + d[i-1] * d[k] * d[j]
                if (m[i][j] > v) :
                    m[i][j] = v
                    p[i][j] = k

    return m, p

if (__name__ == "__main__") :
    data = [2, 3, 4, 3, 2, 4]
    M, P = chain_multiplication(data)

    print_matrix(M)
    print_matrix(P)
