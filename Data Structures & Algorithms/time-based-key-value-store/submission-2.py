class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].insert(0, [timestamp, value])
        else:
            self.hm[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        l, res = 0, ""
        r = len(self.hm[key]) - 1
        
        while l <= r:
            m = (l+r) // 2
            if self.hm[key][m][0] <= timestamp:
                res = self.hm[key][m][1]
                r = m - 1
            else:
                l = m + 1
        return res
