class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # weighted, no direction, connected, n vertices
        # MST is connect all vertices w/o cycels and min posisble total edge weight
        # critical edge means if delete from MST, would cause MST weight to increase
        # pseudo-critical edge can appear in some MSTs, but not all (I guess if equal edge weights? Or how else)..
        # return indices of edges in ANY order
        # seems main way to solve this is with KRUSKAL's - practice UNION-FIND

        # but also can solve with Djkstra's per Solutions, which we attempt below
        # thinking it through, Djkstra's gives shortest path from one node to all others, which is likely not the MST since MST can strt with any arbitrary edge

        # I copied this Djkstra's solution down since was confused by the following to do on my own:
        # 1. appending index to adj, 2. exclude_idx concept, critical & pseudo differences
        # so way I understand it is: 1. build adj list, 2. minimax function for 2 nodes
        # 3. iterate across all edges, compare to minimax removing it, otherwise if == then in pseudo

        for i, edge in enumerate(edges):
            edge.append(i) # didn't realize this worked. Don't need to do edges[i].append(i)...

        adj = defaultdict(list)
        for u, v, w, index in edges:
            adj[u].append((v, w, index))
            adj[v].append((u, w, index)) # to have both sides

        def minimax(src, dst, exclude_index):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)] # import heapq?

            while pq:
                max_w, u = heapq.heappop(pq)
                if u == dst:
                    return max_w # shortest path between 2 nodes, max weight of path
                
                for v, weight, edge_idx in adj[u]: # extend path further
                    if edge_idx == exclude_index:
                        continue
                    new_w = max(max_w, weight)
                    if new_w < dist[v]:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w, v))

            return float('inf') # if not connected

        
        critical, pseudo = [], []
        for u, v, w, idx in edges:
            otherpath = minimax(u, v, idx)
            if w < otherpath:
                critical.append(idx)
            elif w == otherpath: # don't skip, if same weight as this edge
                pseudo.append(idx)
            
        return [critical, pseudo]
        




        