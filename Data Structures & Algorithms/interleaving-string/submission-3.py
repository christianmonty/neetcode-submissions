class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # we could try to break s1 at each index, and match with next part of s3, if doesn't match return False
        # how do we know when to alternate between s1 and s2 characters?
        
        # Going to try to recurse for index of both i and j for s1 and s2 and k for index of s3

        # possible decisions at each recursion step:
        # 1. Either take one char from s1, multiple? or s2 if haven't begun yet (keep taking more)
        # 2. Each step take another char from s1 OR from s2

        # BUT we need to also track # of substrings for s and t to ensure there is not mismatch
        # do we do this by returning a positive number, vs. returning boolean from recursive function?

        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        if len(s1) + len(s2) != len(s3):
            return False # quick check to disqualify invalid strings initially


        def recurse(i: int, j: int, k: int) -> bool:
            if i >= len(s1) and j >= len(s2):
                return True
            elif j >= len(s3):
                return True
            elif i >= len(s1):
                temp = j
                while j < len(s2):
                    if s2[j] != s3[k]:
                        return False
                    # should we be setting dp here?
                    j += 1
                    k += 1
                dp[i][temp] = True
                return True
            elif j >= len(s2):
                temp = i
                while i < len(s1):
                    if s1[i] != s3[k]:
                        return False
                    i += 1
                    k += 1
                dp[temp][j] = True
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            takeleft = takeright = False
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False # can't work
            if s1[i] == s3[k]:
                if dp[i+1][j]:
                    return dp[i+1][j]
                else:
                    takeleft = recurse(i+1, j, k+1)
            if s2[j] == s3[k]: # can't be elif, since can both be true
                if dp[i][j+1]:
                    return dp[i][j+1]
                else:
                    takeright = recurse(i, j+1, k+1)
            
            dp[i][j] = takeleft or takeright
            return takeleft or takeright

        return recurse(0, 0, 0)