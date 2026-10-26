class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        outlist = []
        minheight = 0
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if h > minheight:
                outlist.append(i)
                minheight = h
        
        outlist.sort()
        return outlist