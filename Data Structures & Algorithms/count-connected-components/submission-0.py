from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for i in range(0, n)]
        found = [0] * n
        numcomps = 0

        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)
        
        i = 0
        while i < n:
            while i < n and found[i] == 1:
                i += 1
            if i < n: numcomps += 1
            else:
                break

            temp = adj[i]
            q = deque()
            q.append(i)
            found[i] = 1
            while q:
                node = q.popleft()
                for connection in adj[node]:
                    if not found[connection]:
                        q.append(connection)
                        found[connection] = 1


        return numcomps

        