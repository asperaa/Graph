from collections import deque

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
                self.bfs(i, visited, graph)
                num_components += 1
        return num_components
    
    def bfs(self, s, visited, graph):
        queue = deque()
        queue.append(s)
        visited[s] = True
        
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)