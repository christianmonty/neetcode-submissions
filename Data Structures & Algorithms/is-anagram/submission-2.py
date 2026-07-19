class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False

        for l in s:
            if l not in hms:
                hms[l] = 1
            else:
                hms[l] += 1
        
        for l in t:
            if l not in hmt:
                hmt[l] = 1
            else:
                hmt[l] += 1

        for key in hms:
            if key not in hmt or hms[key] != hmt[key]:
                return False
        
        for key in hmt:
            if key not in hms or hmt[key] != hms[key]:
                return False

        return True