class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # one greedy observation is we want the max balloons to last as long as possible?
        # since multiplicatively, big * big * big is better than taking them out earlier
        # but this problem is DP so

        # say we try to hash an subarray as tuple to get memoized value

        # brute force would be try indexes 0, 1, 2, 3 and add the sum to dp(hashed list)
        # but where does 2D dp come from?
        dp = {}

        def recurse(sublist: List[int]) -> int:
            if len(sublist) == 1:
                return sublist[0]

            if dp.get(tuple(sublist), 0):
                return dp[tuple(sublist)]

            maxval = 0
            for i in range(len(sublist)):
                tempval = sublist[i]
                if i > 0:
                    tempval *= sublist[i-1]
                if i < len(sublist) - 1:
                    tempval *= sublist[i+1]
                newlist = sublist.copy()
                newlist.pop(i)
                curval = tempval + recurse(newlist)
                maxval = max(curval, maxval)
            
            dp[tuple(sublist)] = maxval
            return maxval

        return recurse(nums)
            
            # for each possible index, remove from list, turn to tuple. Check if in dp and if 
        