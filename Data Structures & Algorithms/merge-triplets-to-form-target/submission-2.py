from collections import defaultdict

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # just some thoughts on what I'm noticing
        # for one, maybe we do some sort of min heap (or 3 min heaps for each index)
        # then notice, if find the 5 we need, but 2nd is greater than 2nd needed, or 3rd greater than 3rd needed, discard...
        # could do a 3 hm's of 1st, 2nd and 3rd with their max on others for each
        # what we really need is a triplet with target[0], and it's 1 and 2 <= target 1 and 2
        # then same for next 2. Since if we have all of these, we can do it. Can be same one!
        # oh wait what if already have target, or can i and j be same? No different...
        # so keep track of having at LEAST 2 different ones...
        # wait do we even need hm? Just scan array of triplets once, and track that at least 2 dif and that all 3 numbers are satisfied...maybe we add hm[index of target] = index of triplet that works
        # and then as long as we have hm[0], [1] and [2] and at least one has multiple values, we good

        hm = defaultdict(list)
        extra = False

        for index, t in enumerate(triplets):
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                hm[0].append(index)
            if t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]:
                hm[1].append(index)
            if t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1]:
                hm[2].append(index)
            if t[0] < target[0] and t[1] < target[1] and t[2] < target[2]:
                extra = True
        
        if 0 in hm and 1 in hm and 2 in hm:
            return True
            '''
            if len(hm[0]) > 1 or len(hm[1]) > 1 or len(hm[2]) > 1:
                return True
            if hm[0] != hm[1] or hm[0] != hm[2] or hm[1] != hm[2] or extra:
                return True
            '''
        
        return False

        
