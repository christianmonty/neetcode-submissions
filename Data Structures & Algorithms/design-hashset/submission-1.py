class MyHashSet:

    def __init__(self):
        self.hs = []
        

    def add(self, key: int) -> None:
        for i in self.hs:
            if i == key:
                return
        self.hs.append(key)
        

    def remove(self, key: int) -> None:
        for i in self.hs:
            if i == key:
                self.hs.remove(key) # check syntax
        

    def contains(self, key: int) -> bool:
        for i in self.hs:
            if i == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)