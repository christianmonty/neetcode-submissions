class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # working out the math on paper, despite the initial confusion about generating combinations...
        # I think this is a fairly simple, regular DP problem
        
        dp = [0] * (target + 1)
        dp[0] = 0

        for i in range(target + 1):
            temp = 0
            for n in nums:
                if i - n == 0:
                    temp += 1
                elif i - n > 0:
                    temp += dp[i - n]
            dp[i] = temp

        return dp[target]


        # one thing makes notice DP here. If have target, can iterate from 4 - 1 = 3
        # put everything in nums in a hashmap
        # for everything in nums, 4 - thing in nums = val, dp[val1] + dp[val2] + dp[val3]
        # meaning 4 - 1 = 3, 5 ways to get 3, 4 - 3 = 1, 1 way to get 1. 4 - 2 = 2, only one way to get 2 using only 2's
        # can always test 3 % 2 != 0, can't get 3 from only 2's.
        # but for 4, 4 % 2 = 0, so that's another
        # for 3 can get only 3's, only 1's, then 3 C 2 = 3
        # there is clearly COMBINATION in combo sum IV lol
        
        