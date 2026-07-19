class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # another option is to store in hashset #'s seen within window.
        # once you see duplicate you return true. Otherwise, pop the left element out before advancing left ptr forward
        # oh wait, if you notice something already in set when advancing right forward, return true
        # aha, and then when exhaust the window size, pop left and add next on right. O(k) space in hashset, fixed size window

        hs = set()
        l = 0
        hs.add(nums[l])
        r = l + 1

        while (r-l) < k:
            if nums[r] in hs:
                return True
            hs.add(nums[r])
            r += 1
        # now we have full window size

        while r < len(nums):
            if nums[r] in hs:
                return True
            hs.add(nums[r])
            hs.remove(nums[l])
            l += 1
            r += 1
        return False
'''
        # one way brute force solve is left goes to every index, iterate through k each time so O(nk) time
        # issue is can't just slide the full window across since miss inner duplicates
        # invariant is once you move left pointer, nothing to left of left pointer could be part of duplicate

        # this is brute force

        l = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums) and (r-l) <= k:
                if nums[r] == nums[l]:
                    return True
                r += 1
            l += 1
        return False
    '''
        