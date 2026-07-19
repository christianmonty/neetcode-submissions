class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = maxa = 0
        r = len(heights) - 1

        while l < r:
            
            temp = (r - l) * min(heights[l], heights[r])
            if temp > maxa: maxa = temp

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxa