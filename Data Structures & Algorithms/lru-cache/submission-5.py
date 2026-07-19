class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev  

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])
        
        if len(self.hm) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.hm[lru.key]




