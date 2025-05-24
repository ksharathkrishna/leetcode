class Solution:
    def find(self, x):
            while self.parent[x] != 0: x = self.parent[x]
            return x
            
    def union(self, x , y):
        self.parent[self.find(y)] = self.find(x)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        sol = []
        self.parent = defaultdict(int)
        for u, v in edges:
            if self.find(u) == self.find(v): 
                sol = [u,v]
            else:
                self.union(u,v)
        return sol