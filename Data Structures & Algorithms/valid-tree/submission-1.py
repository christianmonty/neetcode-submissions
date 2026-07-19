class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        hm = set()
        adj = [[] for __ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def recurse(prv: int, nxt: int) -> bool:            
            if nxt not in hm:
                hm.add(nxt)
            else:
                return False

            for items in adj[nxt]:
                if items != prv:
                    ret = recurse(nxt, items)
                    if not ret:
                        return False
            return True

        if n == 1:
            return True

        for index, nodes in enumerate(adj):
            if len(nodes) == 1:
                hm.add(index)
                ret = recurse(index, nodes[0])
                return ret and len(hm) == n
        
        return False