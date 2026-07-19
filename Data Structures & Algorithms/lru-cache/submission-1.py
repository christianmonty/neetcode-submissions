class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.q = []
        self.n = capacity
        

    def get(self, key: int) -> int:
        if key in self.hm:
            self.q.remove(key)
            self.q.append(key)
            return self.hm[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:

        if len(self.q) >= self.n and key not in self.hm:
            remove = self.q.pop(0)
            self.hm.pop(remove)

        if key in self.hm:
            self.q.remove(key)
        self.q.append(key)
        self.hm[key] = value

        
