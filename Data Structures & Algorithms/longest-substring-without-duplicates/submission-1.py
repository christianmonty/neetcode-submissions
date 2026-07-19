class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l, r = 0, 0
        best = 0

        while r < len(s):
            #first we don't know if r-l is valid
            if s[r] not in hm:
                hm[s[r]] = r
            else:
                temp = hm[s[r]] + 1
                l = max(temp, l)
                hm[s[r]] = r
            best = max(best, r-l+1)
            r += 1
        return best
