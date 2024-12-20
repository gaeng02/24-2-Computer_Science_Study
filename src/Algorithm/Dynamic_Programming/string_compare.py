def compare (minindex : list, a : str, b : str) :
    x, y = 0, 0
    
    while (x < len(a) and y < len(b)) :
        
        tx, ty = x, y
    
        
        print(minindex[x][y], end = " ")
        (x, y) = minindex[x][y]
        
        if ((x == tx + 1) and (y == ty + 1)) :
            print(f" {a[tx]} {b[ty]}")
            
        elif ((x == tx) and (y == ty + 1)) :
            print(f" - {b[ty]}")
            
        else :
            print(f" {a[tx]} - ")

def print_matrix (matrix : list) :
    for i in matrix :
        print(i)
    print()
    
def string_compare (str1 : str, str2 : str) : 
    a = list(str1)
    b = list(str2)
    m = len(a) # a
    n = len(b) # b

    penalty = 1 # data가 다를 때
    gap = 2 #한 칸 미루기

    table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]
    minindex = [[ (0,0) for j in range(0, n+1)] for i in range(0, m+1)]
    for j in range (n-1, -1, -1) : table[m][j] = table[m][j+1] + gap
    for i in range (m-1, -1, -1) : table[i][n] = table[i+1][n] + gap

    for i in range (m-1, -1, -1) :
        for j in range(n-1, -1, -1) :
            score = 0
            
            if (a[i] != b[j]) :
                score += penalty
                
            table[i][j] = min(table[i+1][j+1] + score, table[i+1][j] + gap, table[i][j+1] + gap)

            if (table[i][j] == table[i+1][j+1] + score) :  # 불일치
                minindex[i][j] = (i+1, j+1)
            elif (table[i][j] == table[i+1][j] + gap) :  # 틈
                minindex[i][j] = (i+1, j)
            else :
                minindex[i][j] = (i, j+1)

    return table, minindex 

if (__name__ == "__main__") :
    input_1 = "CAGACTAA"
    input_2 = "CCGCTAC"

    table, minindex = string_compare(input_1, input_2)

    compare(minindex, input_1, input_2)

    print_matrix(minindex)
    print_matrix(table)
    

    
    
