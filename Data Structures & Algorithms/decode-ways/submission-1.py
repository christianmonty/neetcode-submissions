class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if not s:
            return 0

        end = len(s) - 1
        front = end - 1
        if int(s[end]) > 0:
            dp[end] = 1

        if len(s) > 1:
            if int(s[front]) > 0:
                dp[front] = dp[front+1]
                tens = int(s[front:front+2])
                if tens <= 26:
                    dp[front] += 1
            front -= 1
            
        while front >= 0:
            if int(s[front]) > 0:
                dp[front] = dp[front+1]
                tens = int(s[front:front+2])
                if tens <= 26:
                    dp[front] += dp[front+2]
            front -= 1
        
        return dp[0]

        