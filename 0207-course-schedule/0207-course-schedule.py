class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        visited = set()
        cp = [False] * numCourses

        def dfs(n, adj, v, cp):
            v.add(n)
            cp[n] = True
            for a in adj[n]:
                if a not in v:
                    if not dfs(a, adj, v, cp): return False
                elif cp[a]:
                    return False
            cp[n]= False
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, adj, visited, cp): return False
        
        return True
