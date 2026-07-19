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
        for item in self.hm[key]:
            if item[0] <= timestamp:
                return item[1]
        return ""
