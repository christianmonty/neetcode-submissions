from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force is count with hashmap but then is O(n) space

        # tricky to think how to do with with constant space

        hm = defaultdict(int)
        threshold = len(nums) // 3
        for n in nums:
            hm[n] += 1
        
        outlist = []
        for index, val in hm.items(): # NOT Enumerate
            if val > threshold:
                outlist.append(index)
        return outlist
            

            

