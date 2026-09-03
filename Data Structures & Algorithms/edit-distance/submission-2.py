class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Solved myself just got caught up by edge case of having future letters at end of word1 match earlier in word2

        # should we try making a 2D DP array with the index of each word?
        # or put 3D as the insert, delete, replace part?
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def recurse(i: int, j: int) -> int:
            if i >= len(word1) and j >= len(word2):
                return 0 # we're done
            elif i >= len(word1):
                count = 0
                while j < len(word2):
                    count += 1 # letters to add to word1
                    j += 1
                return count
            elif j >= len(word2):
                count = 0
                while i < len(word1):
                    count += 1 # letters to delete from word1
                    i += 1
                return count

            if dp[i][j]:
                return dp[i][j] # assume already is min

            # 4 options:
            # 1. (no action) If same character, move both pointers forward with no count
            # 2. (delete) If i next exists, and i next is same as cur j, move i forward twice, j once, count up 1
            # 3. (insert) If j next exists, and j next is same as cur i, move j forward twice, i once, count up 1
            # 4. (replace) else, we just have wrong character mismatch, so we should count up 1, increment both pointers

            # then we return a min of these? Where is the multiple things to try?

            # I first tried to solve this with a clever greedy approach of lookahead, but correct solution is to
            # do the min of various actions as I previously tried
            if word1[i] == word2[j]:
                return recurse(i + 1, j + 1)
            else:
                delete = 1 + recurse(i + 1, j)
                insert = 1 + recurse(i, j + 1)
                replace = 1 + recurse(i + 1, j + 1)
                best = min(delete, insert, replace)
                dp[i][j] = best
                return best
        
        return recurse(0, 0)



            
            

        