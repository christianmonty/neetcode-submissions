class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def recurse(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            if r > m - 1 or c > n - 1 or r < 0 or c < 0:
                return 0
            rret = recurse(r, c+1)
            dret = recurse(r+1, c)
            return rret + dret

        return recurse(0, 0)

        