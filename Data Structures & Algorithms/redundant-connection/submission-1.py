class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
  
        hm = set()
        cycle = set()
        edgeset = set()
        adj = [[] for __ in range(len(edges)+1)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def recurse(prv: int, nxt: int) -> bool:            
            if nxt not in hm:
                hm.add(nxt)
            else: #cycle found!
                cycle.add(nxt)
                return True
                
            for items in adj[nxt]:
                if items != prv:
                    ret = recurse(nxt, items)
                    if ret:
                        if nxt not in cycle:
                            cycle.add(nxt)
                            return True
            return False #no cycle found

        if len(edges) == 1:
            return edges[0]

        done = False
        for index, nodes in enumerate(adj):
            if len(nodes) == 1:
                done = True
                hm.add(index)
                recurse(index, nodes[0])
                break
        if not done:
            for index, nodes in enumerate(adj):
                if len(nodes) == 2:
                    done = True
                    hm.add(index)
                    recurse(index, nodes[0])
                    break

        # now we are sure cycle contains elements of cycle
        for e in edges:
            if e[0] in cycle and e[1] in cycle:
                edgeset.add((e[0], e[1]))

        for i in range(len(edges)-1, -1, -1):
            edge = edges[i]
            tup = (edge[0], edge[1])
            if tup in edgeset:
                return edge

        
        return []