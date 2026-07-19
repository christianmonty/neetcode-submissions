from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # also building this with DFS for practice
        hm = defaultdict(list)
        indeg = [0 for i in range(0, numCourses)]
        toporder = []

        # graph building is same for either case
        for a, b in prerequisites:
            if a == b or b in hm[a]:
                return []
            hm[b].append(a)
            indeg[a] += 1
        
        def dfs(idx: int):
            toporder.append(idx)

            for val in hm[idx]:
                indeg[val] -= 1
                if indeg[val] == 0:
                    dfs(val)
            del hm[idx]
        
        # DFS call
        for idx, val in enumerate(indeg):
            if val == 0:
                dfs(idx)

        return [] if hm else toporder
        

        '''
        # this was BFS and Kahn's algorithm
        hm = defaultdict(list)
        indeg = [0 for i in range(0, numCourses)]
        deq = deque()

        toporder = []

        for a, b in prerequisites:
            if a == b or b in hm[a]:
                return []
            hm[b].append(a)
            indeg[a] += 1
        
        for idx, val in enumerate(indeg):
            if val == 0:
                deq.append(idx)
        
        if not deq:
            return []

        while deq:
            temp = deq.popleft()
            toporder.append(temp)
            for val in hm[temp]:
                indeg[val] -= 1
                if indeg[val] == 0:
                    deq.append(val)
            del hm[temp]
        
        return [] if hm else toporder
        '''