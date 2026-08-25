from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # want thing to note is it's kind of like connectivity problem as a connected to each other letter has some value
        # and then ofc if you have an edge you have reciprocal
        # happy case ab / bc simlpifies to a/c which looks simple
        # but what about degenerate cases like abc / d? Then what is the connection?
        # mixing algebra here seems to complicate everything lol, TBD if there's clean answer

        hm = defaultdict(dict)

        for index, pair in enumerate(equations):
            hm[pair[0]][pair[1]] = values[index]
            hm[pair[1]][pair[0]] = 1 / values[index] # we know this is safe to do
            hm[pair[0]][pair[0]] = 1
            hm[pair[1]][pair[1]] = 1

            # should we add self d->d = 1?
            # should we divide by 'b' ourselves? TBD, could add all of one side to set, then if in 2nd remove, then if in first remove to distill down the essence but might miss pieces in-between. Seems overengineered?
        
        outlist = []
        for q in queries:
            if q[0] not in hm:
                outlist.append(-1)
            elif q[0] in hm and q[1] in hm[q[0]]: # then if edge already in, or reciprocal
                outlist.append(hm[q[0]][q[1]])
            else: # then shortest path, if exists
                visited = set()
                visited.add(q[0]) # first node
                qu = deque()
                qu.append(q[0])
                res = 1.0
                found = False
                while qu and not found: # BFS w/visited nodes
                    temp = qu.pop()

                    # invariant that same path will be same math equation, necessarily
                    for dest in hm[temp]: # this is the second index
                        if dest == q[1]:
                            newpath = hm[q[0]][temp] * hm[temp][dest]
                            outlist.append(newpath)
                            hm[q[0]][dest] = newpath
                            found = True
                            break
                            # if one key includes q[1], then multiply to res, add to outlist and break loop
                        if dest not in visited:
                            # else, add to res, add to visited, add to queue with res
                            visited.add(dest)
                            qu.append(dest)
                            hm[q[0]][dest] = hm[q[0]][temp] * hm[temp][dest] # is this sufficient
                if not found:
                    outlist.append(-1)
        return outlist
                        

                
        
        # now we have the graph made as "adjacency list" in that it's hm[node1] = {node2: cost2, node3: cost3} etc.