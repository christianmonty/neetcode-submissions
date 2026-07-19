class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        s1cp = "" + s1
        s1ar = sorted(s1cp)
        s1cp = "".join(s1ar)
        hs = set()
        hs.add(s1cp)

        i, j = 0, size - 1
        while j < len(s2):
            substring = s2[i:j+1]
            ssarr = sorted(substring)
            substring = "".join(ssarr)
            if substring in hs:
                return True
            i += 1
            j += 1

        return False
        