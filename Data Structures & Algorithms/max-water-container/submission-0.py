class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxw, ml, mr = 0, l, r
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            if water > maxw:
                maxw = water
                ml, mr = l, r
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxw