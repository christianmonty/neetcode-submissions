from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # ok so top sort yea we can pull out by indegree in a queue
        # I guess brute force we could hashmap[prereq] = [list of dependencies]
        # and then each query, do BFS but ONLY add the prereq to queue
        # then pop from queue, add to visited set, then for neighbors not visited add to queue
        # while queue keep doing this, if don't find it output false, else true

        hm = defaultdict(list)

        for p in prerequisites:
            hm[p[0]].append(p[1])
        
        def searchq(uj: int, vj: int) -> bool:
            # assume uj != vj
            visited = set()
            q = deque()

            q.append(uj)
            visited.add(uj)
            while q:
                temp = q.popleft()
                for item in hm[temp]:
                    if item == vj:
                        return True
                    if item not in visited:
                        q.append(item)
                        visited.add(item)
            return False
        
        output = []
        for q in queries:
            res = searchq(q[0], q[1])
            output.append(res)
        return output


