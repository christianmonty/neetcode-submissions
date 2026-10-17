class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo_sort(edges): # factoring this into a function is clever approach
            indegree = [0] * (k+1) # to see how many constraints
            adj = [[] for _ in range(k + 1)]
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1 # top must be above bottom, or left of right

            
            order = []
            q = deque()
            for i in range(1, k+1):
                if not indegree[i]:
                    q.append(i) # put # as first

            while q:
                node = q.popleft()
                order.append(node) # ready to add
                for nextnode in adj[node]:
                    indegree[nextnode] -= 1
                    if not indegree[nextnode]:
                        q.append(nextnode)
            
            return order # once node, must include all nodes

        
        row_order = topo_sort(rowConditions)
        if len(row_order) != k: return [] # this would detect a cycle, some indegree never get to zero

        col_order = topo_sort(colConditions)
        if len(col_order) != k: return [] # also detects a cycle

        res = [[0] * k for _ in range(k)]

        # Below this is trickiest and most unintuitive part for me
        colIndex = [0] * (k + 1)
        for i in range(k):
            colIndex[col_order[i]] = i # to get # -> col index mapping

        for i in range(k):
            res[i][colIndex[row_order[i]]] = row_order[i] # to equal the actual number
        return res















        # constraints: k x k matrix which has each of #'s from 1 to k EXACTLY ONCE. Remaining cells as 0.
        # #'s from 1 to k, when place need to care about constraints
        # what kind of data structure best preserves all these rules? Hashing adj list only gets local order

        # part of me thinks like binary search or starting with tightest bounds...?
        # need a way to detect conflicts too. Remember this is Advanced Graph problem
        # say create Node for 2, above child is 4, left child is 8. 
        # somehow maybe can navigate from starting node, to other nodes (transitively) then to potential order
        # would conflict (two incompatible rules) lead to cycle in our graph?

        # Ah top sort (w/indegrees) enables us to find # with no more further left constraint (or top constraint)
        # then we place number with no left or top constraint, remove indegree from next, keep processing
        # but then I guess we can place along diagonals (k exactly) how else could we place it? Ugh I guess it depends on conditions...Can't we have two numbers placed on same row? as in 2 0 3...next row

        # I didn't get Kahn's (Top Sort BFS) as idea on my own w/o peeking at solution. I overthought it
        # somewhat tricky problem to transform into doable Leetcode, practice these translations again


        