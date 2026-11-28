from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        result = []
        # could make a hashmap of ID -> pq and pull top 5 from each
        hm = defaultdict(list)

        for ID, score in items:
            heapq.heappush(hm[ID], -score)
        
        for ID, pq in hm.items():
            count = 0
            tempsum = 0
            while count < 5:
                tempsum += -heapq.heappop(pq)
                count += 1
            result.append([ID, tempsum // count])
        
        result.sort()
        return result


        