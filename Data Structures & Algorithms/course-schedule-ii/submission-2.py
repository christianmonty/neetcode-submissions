class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ind = [0] * numCourses #indegree array to track for each node
        adj = [[] for i in range(numCourses)] #to track all prereq relationships
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            ind[pair[0]] += 1

        q = []
        outlist = []

        for index, val in enumerate(ind):
            if val == 0:
                outlist.append(index)
                q.append(index)
        
        while q:
            index = q.pop(0)
            for item in adj[index]:
                ind[item] -= 1
                if ind[item] == 0:
                    q.append(item)
                    outlist.append(item)
        
        for val in ind:
            if val != 0:
                return []
        return outlist