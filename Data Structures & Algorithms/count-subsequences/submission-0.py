class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # had to look at hints to come up with answer, but implemented myself

        dp = {}
        # [[0 for _ in range(len(t))] for _ in range(len(s))]

        def recurse(i: int, j: int) -> int:
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            if (i, j) in dp:
                return dp[i, j]
            # now we try skip, or use current index if == at same pos of s and t
            skip = recurse(i + 1, j)
            use = 0
            if s[i] == t[j]:
                use = recurse(i + 1, j + 1)
            
            dp[(i, j)] = skip + use
            return dp[(i, j)]

        return recurse(0, 0)
