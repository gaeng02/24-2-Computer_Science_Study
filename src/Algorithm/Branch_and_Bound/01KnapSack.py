# Depth First Search
def knapsack_dfs (i, profit, weight) :
    global best_set
    global max_profit

    if ((weight <= W) and (profit > max_profit)) :
        max_profit = profit
        best_set = include.copy()

    if (promising(i, weight, profit)) :
        i += 1
        include[i] = 1
        knapsack_dfs(i, profit + p[i], weight + w[i])
        include[i] = 0
        knapsack_dfs(i, profit, weight)

def promising (i, weight, profit) :
    global max_profit

    if (weight >= W) : return False

    bound = profit
    j = i + 1

    while ((j < n) and (weight + w[j] <= W)) :
        weight += w[j]
        bound += p[j]
        j += 1

    if (j < n) :
        bound += (W - weight) * (p[j] / w[j])
        
    return (bound > max_profit)

# Breadth First Search 
import queue

class Node :
    def __init__(self, level, weight, profit, include) :
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

    def __str__  (self) :
        return  f"{self.level}, {self.weight}, {self.profit}, {self.include}"


def knapsack_bfs () :
    global best_set
    global max_profit

    q = queue.Queue()

    v = Node(-1, 0, 0, include.copy())
    q.put(v)

    while (not q.empty()) :
        v = q.get()

        if (v.level == n - 1) : 
            if (v.profit > max_profit) :
                best_set = v.include.copy()
                max_profit = v.profit
                
        else :
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1], v.include.copy())
            u.include[u.level] = 1
            v.level += 1

            if ((u.weight <= W) and (u.profit > max_profit)) :
                best_set = u.include.copy()
                max_profit = u.profit
                
            if (Bound(u) > max_profit) :
                q.put(u)

            u = Node(v.level, v.weight, v.profit, v.include.copy())
            
            if (Bound(u) > max_profit) :
                q.put(u)
                

def Bound (u : Node) :
    
    if (u.weight > W) : return 0

    bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    while ((j < n) and (total_weight + w[j] <= W)) :
        total_weight += w[j]
        bound += p[j]
        j += 1

    if (j < n) :
        bound += (W - total_weight) * (p[j] / w[j])
    
    return bound


if (__name__ == "__main__") :
    W = 7
    p = [10, 12, 4, 18]
    w = [5, 6, 4, 3]
    
    n = len(p)


    # DFS
    include = [0] * n
    best_set = [0] * n
    max_profit = 0
    
    knapsack_dfs(-1, 0, 0)
    
    print(best_set)
    print(max_profit)


    # BFS
    include = [0] * n
    best_set = [0] * n
    max_profit = 0

    knapsack_bfs()

    print(best_set)
    print(max_profit)

     
