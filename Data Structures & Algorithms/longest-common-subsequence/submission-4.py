class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Had to look at hints to get unstuck, seems like simpler method is as follows
        # Match up char by char, and then if letters match remove recent let of each & take diagonal
        # if letters don't match, try removing a letter from either and then then max of those
        # Gotta get used to these patterns!

        # convention we'll used is text1 is rows, text2 iw columns

        # ended up having to copy from solutions to fully understand / implement it
        dp = [[0 for __ in range(len(text2)+1)] for __ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
            
        
        return dp[0][0]
