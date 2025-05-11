class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list from prerequisites
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)  # v -> u means u depends on v

        visited = set()  # Tracks all nodes that have been fully processed
        currPath = [False] * numCourses  # Tracks nodes in the current DFS path

        # DFS function to detect cycle
        def dfs(node, adj, visited, currPath):
            visited.add(node)         # Mark node as visited
            currPath[node] = True     # Mark node as part of current path
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    # Recurse into unvisited neighbor
                    if not dfs(neighbor, adj, visited, currPath):
                        return False
                elif currPath[neighbor]:
                    # Found a back edge (cycle)
                    return False

            currPath[node] = False    # Remove node from current path
            return True

        # Check all nodes, in case graph is disconnected
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, adj, visited, currPath):
                    return False  # Cycle detected

        return True  # No cycles found, all courses can be finished
