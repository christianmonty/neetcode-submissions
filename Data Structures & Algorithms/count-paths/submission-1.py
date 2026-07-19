class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for __ in range(n)] for __ in range(m)]

        dp[0][0] = 1
        r, c = 0, 0
        while r < m:
            c = 0
            while c < n:
                if r - 1 >= 0:
                    dp[r][c] += dp[r-1][c]
                if c - 1 >= 0:
                    dp [r][c] += dp[r][c-1]
                c += 1
            r += 1

        return dp[m-1][n-1]






        """ Recursive solution below. Will do DP now
        def recurse(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            if r > m - 1 or c > n - 1:
                return 0
            rret = recurse(r, c+1)
            dret = recurse(r+1, c)
            return rret + dret

        return recurse(0, 0)

        """

        