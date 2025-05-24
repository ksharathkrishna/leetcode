class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjacency list from prerequisites
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)  # v -> u means u depends on v

        visited = set()  # Tracks all nodes that have been fully processed
        currPath = [False] * numCourses  # Tracks nodes in the current DFS path

        # DFS function to detect cycle
        def dfs(node, adj, visited, currPath, ans):
            visited.add(node)         # Mark node as visited
            currPath[node] = True     # Mark node as part of current path
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    # Recurse into unvisited neighbor
                    if not dfs(neighbor, adj, visited, currPath, ans):
                        return False
                elif currPath[neighbor]:
                    # Found a back edge (cycle)
                    return False

            currPath[node] = False    # Remove node from current path
            ans.append(node)
            return True

        # Check all nodes, in case graph is disconnected
        ans = []
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, adj, visited, currPath, ans):
                    return []  # Cycle detected

        return ans[::-1]  # No cycles found, all courses can be finished