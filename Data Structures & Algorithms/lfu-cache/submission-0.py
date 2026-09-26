from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = OrderedDict() # for the LRU order
        self.freq = defaultdict(set) # freq # -> {key1, key2, key3 etc.} (set of keys)
        # for frequency to key mappings
        
    def get(self, key: int) -> int:
        if key in self.hm:
            self.hm.move_to_end(key)
            fr = self.hm[key][0]
            val = self.hm[key][1]
            self.freq[fr].remove(key)
            self.freq[fr + 1].add(key)
            self.hm[key] = (fr + 1, val) # increment use counter
            return self.hm[key][1]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm.move_to_end(key)
            fr = self.hm[key][0]
            self.freq[fr].remove(key)
            self.freq[fr + 1].add(key)
            self.hm[key] = (fr + 1, value)# increment use counter
            return
        if len(self.hm) >= self.capacity:
            count = 1
            while len(self.freq[count]) == 0:
                count += 1
            # eviction
            # collect lower # frequencies
            validset = self.freq[count] # list of valid items

            # then evict one with most front order in OrderedDict...
            temp = None
            for k, values in self.hm.items():
                if k in validset: # already starting from left!
                    temp = k
                    break
            if temp is not None: # can finally evict
                del self.hm[temp]
                self.freq[count].remove(temp)
        self.hm[key] = (1, value)
        self.freq[1].add(key)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# recall Least Recently after use, put to beg of list, priority highest
# Review how I built LRU! because still need that to break ties...
# LRU is OrderedMap (hashmap over linked list underneath for order property)

# here instead we could have hashmap of key -> frequency and inc on moving around
# BUT we also need some sort of binary heap or something where we have low use -> high use
# to make evictions fast for puts we need a binary heap for sorted order (pre-tie)
# but then updating binary heap is expensive each time to update frequency...
# oh wait in OrderedMap we can store key = (freq, value) and move to last when new
# and update frequency by hm[key] = (new freq, value)
# then the issue is just: how do we isolate the smallest frequencies? I still like bin heap
# average time complexity works unless capacity reached? idk since O(1) != O(logn)
# wait what about two OrderedMaps? One for LRU (easier), one for LFU (can order based on counter)?
# can you have a hashmap point to entries of a PriorityQueue or no?
