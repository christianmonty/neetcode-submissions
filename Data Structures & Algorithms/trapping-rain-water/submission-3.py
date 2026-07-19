class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = maxa = 0

        while i < len(height):
            maxl = maxr = height[i]

            for j in range(0, i):
                if height[j] > maxl: maxl = height[j]

            for j in range(i, len(height)):
                if height[j] > maxr: maxr = height[j]

            maxa += min(maxl, maxr) - height[i]
            i += 1
        
        return maxa





















'''
        # Attempt 1: didn't full work. Mixed the running max parts!!
        # this approach is 2 pointers + stack, we'll see if works without DP
        l = maxa = 0
        while l < len(height) and height[l] == 0:
            l += 1
        
        r = l + 1
        end = False
        while r < len(height):
            # check area here - what's on stack
            stack = []

            while height[r] < height[l]:
                stack.append(height[r])
                r += 1
                if r >= len(height):
                    end = True
                    break 

            if not end:
                temparea = min(height[l], height[r]) * (r - l - 1)
                
                while stack:
                    temparea -= stack.pop()
                maxa += temparea

                l = r
                r = l + 1
        
        return maxa
'''
