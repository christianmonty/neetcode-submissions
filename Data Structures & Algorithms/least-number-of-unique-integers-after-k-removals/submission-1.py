class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # wait I misunderstood question, remove FEWEST counts first
        hm = defaultdict(int)
        pq = []        
        # need to remove the occurences, but return the # unique items (set). So have both pq & set
        for a in arr:
            hm[a] += 1

        for key, value in hm.items():
            heapq.heappush(pq, (value, key))

        count = 0
        while pq and count < k:
            val, key = heapq.heappop(pq)
            hm[key] -= 1
            if hm[key] == 0:
                del hm[key]
            else:
                heapq.heappush(pq, (val - 1, key))
            count += 1
        
        return len(hm.keys())

