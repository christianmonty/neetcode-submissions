class Solution:
    def isPalindrome(self, s: str) -> bool:
        #basic two pointer solution is start at front and end. If even, you're good, If odd, then when i == j, stop

        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True