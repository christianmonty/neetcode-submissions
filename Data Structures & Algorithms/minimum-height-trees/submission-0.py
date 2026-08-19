from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # without cycles immediately makes me think of top sort (indegrees)
        # but not directed graph, so unlikely top sort?

        # since level, I'm thinking run BFS on each possible option
        # don't even think of the trees as a Tree problem but as a graph problem
        # root added to queue with level 1 in tuple, then add kids w/+1 depth
        # return the max height for each tree in array, and then O(1) find the min & then return
        # wait but first must build a hashmap of all node[edges]
        # and then we'll used a visited() set for each BFS
        hm = defaultdict(list)
        heights = [0] * n

        for e in edges:
            hm[e[0]].append(e[1])
            hm[e[1]].append(e[0])

        for i in range(n):
            visited = set()
            q = deque()
            q.append((i, 0))
            visited.add(i)

            height = 0

            while q:
                temp = q.popleft()
                newheight = temp[1] + 1
                for item in hm[temp[0]]:
                    if item not in visited:
                        q.append((item, newheight))
                        visited.add(item)
                        if newheight > height:
                            height = newheight
            heights[i] = height
        
        minheight = float('inf')
        outlist = []
        for index, val in enumerate(heights):
            if val < minheight:
                minheight = val
                outlist = [index]
            elif val == minheight:
                outlist.append(index)
        return outlist


            





        