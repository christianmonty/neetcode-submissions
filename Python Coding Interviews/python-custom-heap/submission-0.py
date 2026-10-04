import heapq
from typing import List

# heapq tuple custom sorting...first element priority, then 2nd element

def get_reverse_sorted(nums: List[int]) -> List[int]:

    outlist = []
    heap = []
    for num in nums:
        pair = (-num, num) # to sort entire thing reversed, what do we need tuple tho?
        heapq.heappush(heap, pair)
    
    while heap:
        pair = heapq.heappop(heap)
        outlist.append(pair[1])
    return outlist
    



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
