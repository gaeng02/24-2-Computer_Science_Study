import numpy as np

def strassen (n, A, B, C) :
    '''
    두개의 n * n 행렬의 곱을 구하라
    input :
    - int n : size of col and row of matrix
    - list A, B : multiplied matrix
    - list C : none matrix
    output : C (result matrix)
    '''
    threshold = 2

    if (n <= threshold) : C = np.array(A) @ np.array(B); return C

    m = n // 2
    A_11 = np.array([[A[rows][cols] for cols in range(m)] for rows in range(m)])
    A_12 = np.array([[A[rows][cols + m] for cols in range(m)] for rows in range(m)])
    A_21 = np.array([[A[rows + m][cols] for cols in range(m)] for rows in range(m)])
    A_22 = np.array([[A[rows + m][cols + m] for cols in range(m)] for rows in range(m)])

    B_11 = np.array([[B[rows][cols] for cols in range(m)] for rows in range(m)])
    B_12 = np.array([[B[rows][cols + m] for cols in range(m)] for rows in range(m)])
    B_21 = np.array([[B[rows + m][cols] for cols in range(m)] for rows in range(m)])
    B_22 = np.array([[B[rows + m][cols + m] for cols in range(m)] for rows in range(m)])

    M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
    M1 = strassen(m, (A_11 + A_22), (B_11 + B_22), M1)
    M2 = strassen(m, (A_21 + A_22), B_11, M1)
    M3 = strassen(m, A_11, (B_12 - B_22), M1)
    M4 = strassen(m, A_22 , (B_21 - B_11), M1)
    M5 = strassen(m, (A_11 + A_12) , B_22, M1)
    M6 = strassen(m, (A_21 - A_11) , (B_11 + B_12), M1)
    M7 = strassen(m, (A_12 - A_22) , (B_21 + B_22), M1)

    C = np.vstack([np.hstack([M1+M4 -M5 + M7, M3 + M5]), np.hstack([M2 + M4, M1 + M3 - M2 + M6])])
    return C


if (__name__ == "__main__") :
    n = 4
    A = [[1,2,0,2], [3,1,0,0], [0,1,1,2], [2,0,2,0]]
    B = [[0,3,0,2], [1,1,4,0], [1,1,0,2], [0,5,2,0]]
    
    C = [[0 for cols in range(4)] for rows in range(4)]
    C = strassen(4, A, B, C)
    
    print(C)
    # result ::
    # [2, 15, 12,  2]
    # [1, 10, 4, 6]
    # [2, 12, 8, 2] 
    # [2, 8, 0, 8]
