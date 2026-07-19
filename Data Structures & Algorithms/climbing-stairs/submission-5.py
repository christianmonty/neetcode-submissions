class Solution:
    def climbStairs(self, n: int) -> int:

        stairs = [0 for i in range(0, n)]
        stairs[n-1] = 1

        if n > 1:
            stairs[n-2] = 2

        for i in range(n-3, -1, -1):
            stairs[i] = stairs[i+2] + stairs[i+1]
        
        return stairs[0]
