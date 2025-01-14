
class Solution:
    def countComponents(self, n, edges):
        visited = [False for _ in range(n)]
        graph = {i: [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        num_components = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i, graph, visited)
                num_components += 1
        return num_components
    
    def dfs(self, i, graph, visited):
        if visited[i]:
            return
        visited[i] = True
        for neighbour in graph[i]:
            self.dfs(neighbour, graph, visited)
            
    