class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.hm:
            self.hm[key][1] = self.time 
            return self.hm[key][0]
        return -1
        
    def put(self, key: int, value: int) -> None:
        self.time += 1

        self.hm[key] = [value, self.time]

        if len(self.hm) > self.capacity:
            # remove LRU key
            mintime = float('infinity')
            minkey = key
            for k in self.hm:
                if self.hm[k][1] < mintime:
                    mintime = self.hm[k][1]
                    minkey = k
            del self.hm[minkey]


