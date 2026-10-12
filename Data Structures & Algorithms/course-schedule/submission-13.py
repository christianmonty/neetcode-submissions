from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # here is attempt at DFS based cycle detection with visited set for current path
        # copying solution of have node -> prereqs adjacency list (opposite of BFS Kahn's)
        # also then add nodes seen to current path set

        prereqs = [[] for i in range(numCourses)]
        for node, prereq in prerequisites:
            prereqs[node].append(prereq)

        # where to start the dfs call?
        visited = set()


        def dfs(node: int) -> bool:
            if node in visited:
                return False

            if prereqs[node] == []:
                return True

            visited.add(node)

            for n in prereqs[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            prereqs[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        '''

        # below is what I naturally do to solve, Kahn's algorithm for top sort
        
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
        '''