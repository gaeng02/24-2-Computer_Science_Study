def promising (i, weight, total, current_sum) :
    return ((current_sum + total >= W) and (current_sum == W or current_sum + weight[i + 1] <= W))

def sum_of_subsets (i, weight, total, current_sum, include, solutions, nodes) :
    nodes += 1
    
    if promising(i, weight, total, current_sum) :
        
        if (current_sum == W) : solutions.append(include.copy())
        
        else :
            
            include[i + 1] = 1
            solutions, nodes = sum_of_subsets(i + 1, weight, total - weight[i + 1], current_sum + weight[i + 1], include, solutions, nodes)
            
            include[i + 1] = 0
            solutions, nodes = sum_of_subsets(i + 1, weight, total - weight[i + 1], current_sum, include, solutions, nodes)
            
    return solutions, nodes


if (__name__ == "__main__") :
    
    w = [1, 2, 4, 8]
    W = 6

    n = len(w)
    include = [0] * n
    total = sum(w)

    solutions, nodes = sum_of_subsets(-1, w, total, 0, include, [], 0)

    print(f" Items :: {w}")
    print(f" Weight :: {W}")

    print(f" The number of solutions :: {len(solutions)}")
    for solution in solutions : print(f" {solution}")
    print(" The total number of nodes ::", nodes)
