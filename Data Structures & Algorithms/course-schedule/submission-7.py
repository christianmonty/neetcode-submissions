from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # implement Kahn's algorithm as BFS too!
        deq = deque() # for BFS
        hm = defaultdict(list) # for adjacency list, need list factory for default as empty list
        indeg = [0] * numCourses # for indegrees

        for a, b in prerequisites:
            if a == b or b in hm[a]:
                return False
            hm[b].append(a)
            indeg[a] += 1

        for index, val in enumerate(indeg):
            if val == 0:
                deq.append(index)

        if not deq:
            return False

        while deq:
            temp = deq.popleft()
            for val in hm[temp]:
                indeg[val] -= 1 # check works
                if indeg[val] == 0:
                    deq.append(val)
            del hm[temp]
        
        return not deq



'''
        # dfs with backtracking approach
        hm = {i: [] for i in range(0, numCourses)}
        for idx, value in prerequisites:
            hm[idx].append(value)

        hs = set()

        def dfs(idx: val) -> bool:
            # base case: if node itself has no edges
            if len(hm[idx]) < 1:
                return True
            for val in hm[idx]:
                if val not in hs:
                    hs.add(val)
                    res = dfs(val)
                    if res:
                        hm[idx].remove(val)
                        hs.remove(val)
                    else:
                        return False
                else:
                    return False
            return True

        for idx in hm:
            res = dfs(idx)
            if not res: return False

        return True
'''