from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # we have to build a prerequiste graph
        # we go through every node, create adjacency list of node 1, which nodes it connects to
        # then separate indegree array for num of course for each
        # then we add all at 0 indegree to q, and go from there
        # once queue empty, either all indegree map is 0 or is not, meaning can't
        adj = defaultdict(list) # key course : value courses we are prereq for
        indeg = [0 for _ in range(numCourses)]
        q = deque()

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1

        for i, val in enumerate(indeg):
            if val == 0:
                q.append(i)

        while q:
            prereq = q.popleft()

            for node in adj[prereq]:
                indeg[node] -= 1
                if indeg[node] == 0:
                    q.append(node)


        return True if sum(indeg) == 0 else False