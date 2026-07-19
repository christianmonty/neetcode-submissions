class Solution:
    def longestPalindrome(self, s: str) -> str:
        #new attempt using DP

        n = len(s)
        dp = [[False]*n for __ in range(n)] #need to still make double array!!

        res, resindex = 0, 0
        

        for i in range(n-1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j] and ((j - i + 1) <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if len(s[i:j]) > res:
                        res = len(s[i:j])
                        resindex = i

        return s[resindex : resindex+res+1]
        
        
        
        
        
        '''
        #my attempt at adapting even/odd pointers for O(n^2) time and O(1) space
        longest = ""

        for i in range(len(s)):
            f, l = i, i
            while f >= 0 and l < len(s) and s[f] == s[l]:
                temp = s[f:l+1]
                if len(temp) > len(longest):
                    longest = temp
                f -= 1
                l += 1

            f, l = i, i+1
            while f >= 0 and l < len(s) and s[f] == s[l]:
                temp = s[f:l+1]
                if len(temp) > len(longest):
                    longest = temp
                f -= 1
                l += 1

        return longest
        
        #below didn't work for all test cases unfortunately
        if len(s) <= 1:
            return s

        if s == s[::-1]:
            return s

        s1 = self.longestPalindrome(s[1:])
        s2 = self.longestPalindrome(s[:-1])


        if len(s1) > len(s2):
            return s1
        else:
            return s2
        '''

