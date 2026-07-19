class Solution:
    def validPalindrome(self, s: str) -> bool:

        # I overcomplicated with a bunch of conditionals. As simple as helper function + skip one
        # I should have thought pass helper the pointers, not the substring itself! Duh

        # Initial approach below, is O(n^2) runtime but we can do better
        # recall can also look if s = s[::-1]

        def isPalindrome(l: str, r: str) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if isPalindrome(0, len(s)-1):
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
            l += 1
            r -= 1
        
        return True