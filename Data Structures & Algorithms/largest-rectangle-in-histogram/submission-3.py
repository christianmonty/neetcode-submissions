class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # below is trying to implement basic Slack implementation

        leftmost = [-1] * len(heights)

        stack = []
        # fill out leftmost
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)
        
        rightmost = [len(heights)] * len(heights)
        stack = []
        # find rightmost
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)

        
        maxArea = 0
        for i in range(len(heights)):
            leftmost[i] += 1
            rightmost[i] -= 1
            tempMax = (rightmost[i] - leftmost[i] + 1) * heights[i]
            maxArea = max(maxArea, tempMax)

        return maxArea




        '''
        # issue with this initial attempt is we're throwing away state...
        # instead must track ALL lower heights

        # ok stack comes in handy somewhere, maybe popping off and taking:
        # max(pop count * min height seen), OR cur height * 1? If reset, greedily take?
        # or max seen so far, in which case do what? Could do dp as popping back?

        # invariant is once you take a step back, if go lower, that's max height you have
        # note if get to new min, then it's either min * count infront OR prev max, or new if go up
        # basically if go up, either take inclusion (extension) on min, OR reset newmax * 1, or prev max
        # max seen so far as bounce back, then curmax which is nums of rows * min height, or reset cur rows

        stack = []
        for h in heights:
            stack.append(h)

        gmax = curmax = curmin = 0
        rows = 0
        while stack:
            if self:
                rows += 1
            else:
                rows = 0
            temp = stack.pop()
            self = temp * 1
            if not curmin or temp < curmin:
                curmin = temp
            curmax = curmin * rows
            if self >= curmax:
                rows = 1
                curmax = temp
                curmin = temp
            gmax = max(self, curmax, gmax)
        return gmax
        '''
        
        