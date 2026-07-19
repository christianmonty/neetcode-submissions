class Solution:
    def numSquares(self, n: int) -> int:
        # brute force is calculate all perfect squares in an array from 1^2 to 100^2
        # then work backwards from largest, try substracting and keep going

        # so we could build up an array of n from 1 to 10,000. All the perfect squares have 1
        # and then start at 2 and say try 2 - perf squares + value at minus, min of those
        # or say we're at end, 999. If we remove by a single perf sq < 999, that is 1 + value[999-single perf sq] and so we can min of those + 1
        dp = [n] * 10001
        dp[0] = 0
        pers = []
        for i in range(1, 101):
            ps = i * i
            dp[ps] = 1
            pers.append(ps)
            # do we also need perfs stored in set somewhere?

        for i in range(1, n+1):
            leastnum = n
            for j in range(0, len(pers)):
                persquare = pers[j]
                if i - persquare < 0:
                    break
                leastnum = min(leastnum, 1 + dp[i - persquare]) # this must occur within the inner loop
            dp[i] = leastnum
        
        return dp[n]
