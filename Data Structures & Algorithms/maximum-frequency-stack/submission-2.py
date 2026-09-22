import heapq
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.counter = 0 # should this be time? (recency) rather than size I assume
        self.freq = []
        self.closest = defaultdict(list) # we're going to use this to store recency of when popped
        

    def push(self, val: int) -> None:
        # if push, we can add to hm for count. And then put on pq for frequency?
        self.counter += 1
        
        if val not in self.closest:
            heapq.heappush(self.freq, (-1, -self.counter, val))
        else:
            # invariant is we KNOW it must be in pq

            # maybe pop items from heapq into another heapq until find item then update
            excesspq = []
            
            while self.freq[0][2] != val:
                temp = heapq.heappop(self.freq)
                heapq.heappush(excesspq, temp)
            negfreq, negselfcounter, val = heapq.heappop(self.freq) # error check
            heapq.heappush(self.freq, (negfreq - 1, -self.counter, val)) # update push
            while excesspq:
                temp = heapq.heappop(excesspq)
                heapq.heappush(self.freq, temp)
        
        self.closest[val].append(self.counter)
            
        

    def pop(self) -> int:
        negfreq, negselfcounter, val = heapq.heappop(self.freq)
        frequency = -negfreq
        selfcounter = -negselfcounter # don't need to incremnt that now
        self.closest[val].pop()

        if negfreq + 1 < 0:
            # add back if still numbers left. Add next most recent to top
            heapq.heappush(self.freq, (negfreq + 1, -self.closest[val][-1], val))
        else:
            del self.closest[val] # delete and don't add back
        
        return val

        # want max frequency and max counter (stack top) so do neg for both
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()