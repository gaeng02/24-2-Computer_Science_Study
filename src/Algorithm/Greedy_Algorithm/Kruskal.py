class Kruskal () :

    def __init__ (self, graph : dict) :
        self.parent = dict()
        self.rank = dict()
        self.graph = graph
        self.mst = self.kruskal()
        # 입력된 그래프의 간선을 이용해 Kruskal 알고리즘 수행 후, mst 변수에 최소 신장 트리를 저장
        
    def make_singleton_set (self, vertex : str) :
        self.parent[vertex] = vertex # 각 정점은 자기 자신을 부모로 가짐
        self.rank[vertex] = 1 # 트리의 깊이(rank)는 1

    def find (self, vertex : str) :
        if (self.parent[vertex] != vertex) :
            self.parent[vertex] = self.find(self.parent[vertex]) # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 -> 경로 압축
        return self.parent[vertex]

    def union(self, x : str, y : str) :
        if (x != y) :
            if (self.rank[x] > self.rank[y]) :
                self.parent[y] = x
                self.rank[x] += self.rank[y]
                # 깊이가 더 낮은 트리를 깊이가 높은 트리에 병합
            else :
                self.parent[x] = y
                self.rank[y] += self.rank[x]
        
    def kruskal (self) :
        edges = sorted(self.graph["edges"]) # 간선 정렬: 그래프에 있는 간선을 가중치를 기준으로 오름차순 정렬
        F = set()

        for vertex in self.graph["vertices"] :
            self.make_singleton_set(vertex) # 각 정점에 대해 make_singleton_set 호출

        for edge in edges :
            w, i, j = edge
            x = self.find(i)
            y = self.find(j)
            # find를 사용하여 두 정점이 속한 집합을 확인

            if (x != y) :
                self.union(x, y) # 서로 다른 집합에 속한 경우 union을 사용해 병합
                F.add(edge) # 선택된 간선은 최소 신장 트리의 일부로 추가
                
        return F

    def return_mst (self) :
        return self.mst


if (__name__ == "__main__") :
    graph = { 'vertices': ['A', 'B', 'C', 'D', 'E'], 
          'edges': set([(1, 'A', 'B'), (3, 'A', 'C'), (3, 'B', 'C'), (6, 'B', 'D'), (4, 'C', 'D'), (2, 'C', 'E'), (5, 'D', 'E')])}

    mst = Kruskal(graph)
    print(mst.return_mst())
