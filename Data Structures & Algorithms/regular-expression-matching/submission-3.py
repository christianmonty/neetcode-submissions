class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # got the shape of this solution on my own once I understood problem was match EXACTLY and that a*
        # meant you had to look ahead vs. process as you go
        # Also the base cases were very WEIRD and unusual for me!!
        
        dp = {}
        def recurse(i: int, j: int) -> bool:
            if j >= len(p):
                return i >= len(s) # must both be the case
            if i >= len(s):
                # This part is TRICKY and requires delicate care
                return j + 1 < len(p) and p[j+1] == "*" and recurse(i, j + 2)

            if (i, j) in dp:
                return dp[(i, j)]
            
            let = s[i]
            match = p[j]
            dp[(i,j)] = False

            if j < len(p) - 1 and p[j+1] == '*':
                first = False
                if let == match or match == '.':
                    first = recurse(i+1, j) # repeat path
                second = dp[(i,j)] = recurse(i, j + 2) # skip star path path
                dp[(i,j)] = first or second
            elif let == match or match == '.':
                dp[(i,j)] = recurse(i+1, j+1)
            return dp[(i,j)]



        return recurse(0, 0)