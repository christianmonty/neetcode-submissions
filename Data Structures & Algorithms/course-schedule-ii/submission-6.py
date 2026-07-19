from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

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
        