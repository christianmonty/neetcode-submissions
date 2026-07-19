class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = dict()
        dt = dict()

        for i in s:
            if i in ds:
                ds[i] = ds[i] + 1
            else:
                ds[i] = 1

        for i in t:
            if i in dt:
                dt[i] = dt[i] + 1
            else:
                dt[i] = 1

        for i in s:
            if i not in t or ds[i] != dt[i]:
                return False

        for i in t:
            if i not in s or ds[i] != dt[i]:
                return False

        return True