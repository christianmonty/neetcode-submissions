class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # one way brute force solve is left goes to every index, iterate through k each time so O(nk) time
        # issue is can't just slide the full window across since miss inner duplicates
        # invariant is once you move left pointer, nothing to left of left pointer could be part of duplicate

        l = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums) and (r-l) <= k:
                if nums[r] == nums[l]:
                    return True
                r += 1
            l += 1
        return False
        