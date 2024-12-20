class dijkstra () :

    def __init__ (self, W) :
        self.w = W
        self.n = len(W)

        self.f = set()
        self.touch = [0] * self.n
        self.length = [0] * self.n
        self.save_length = [0] * self.n

        for i in range (1, self.n) : self.length[i] = self.w[0][i]

        self.do_dijkstra()

    def do_dijkstra (self) :
        inf = 1000

        for i in range (1, self.n) : 
            min_length = inf
            
            for j in range(1, self.n) :
                if (0 <= self.length[j] < min_length) :
                    min_length = self.length[j]
                    vnear = j

            edge = (self.touch[vnear], vnear)
            self.f.add(edge)

            for k in range (1, self.n) :
                if ((self.length[vnear] + self.w[vnear][k]) < self.length[k]) :
                    self.length[k] = self.length[vnear] + self.w[vnear][k]
                    self.touch[k] = vnear

            self.save_length[vnear] = self.length[vnear]
            self.length[vnear] = -1


if (__name__ == "__main__") :
    
    inf = 1000
    w = [[0, 2, 3, inf, inf, 4],
         [inf, 0, 4, 5, 3, inf],
         [inf, inf, 0, 6, 2, inf],
         [inf, inf, inf, 0, 2, inf],
         [inf, inf, inf, inf, 0, inf],
         [inf, inf, inf, inf, 1, 0]]

    D = dijkstra(w)
    node = ['A', 'B', 'C', 'D', 'E', 'F']

    print(D.f)
    print(D.save_length)
    
    for i in range (1, len(w)) :
        path = []
        current = i
        while (current != 0) :
            path.insert(0, node[current])
            current = D.touch[current]
        path.insert(0, node[0])
        distance = D.save_length[i]
        print(f"Path '{ ' → '.join(path):}' :: Distance : { distance }")

