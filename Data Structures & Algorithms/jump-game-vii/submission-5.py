class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # is this DP for the paths, and then greedy for furthest path?
        goal = len(s) - 1
        if s[-1] != '0' or s[0] != '0':
            return False # trivially
        
        dp = [False for _ in range(len(s))]
        dp[len(s) - 1] = True
        j = len(s) - 1

        # my original approach was O(n^2) but can make this O(n) with clever only update j if new
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0' and dp[i]:
                j = min(j, i - minJump)
                while j >= 0 and j >= i - maxJump:
                    if s[j] == '0':
                        dp[j] = True
                    j -= 1
        
        return dp[0]




        '''
        # below is my first attempt

        # since greedy, makes me think you always want to take maxjump, since can always scale down if needed

        # WTF is this not greedy, but DP??!?

        i = 0
        while i < len(s) - 1:
            j = min(i + maxJump, len(s) - 1)
            if j - i < minJump:
                return False # issue here cwhen don't have access to other jumps!!
            while j >= i + minJump:
                if j == len(s) - 1:
                    if s[j] == '1':
                        return False
                    else:
                        return True
                elif s[j] == '0':
                    i = j
                    break
                elif s[j] == '1' and j == i + minJump:
                    return False # no more jump to be made!
                else:
                    j -= 1
        return True # means i reached the end

        '''