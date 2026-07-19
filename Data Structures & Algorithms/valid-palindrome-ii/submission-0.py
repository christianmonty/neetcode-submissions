class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(w: str) -> bool:
            l, r = 0, len(w) - 1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            if isPalindrome(s[:i] + s[i+1:len(s)]):
                return True
        
        return False