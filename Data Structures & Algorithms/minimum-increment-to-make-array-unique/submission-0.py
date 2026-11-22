class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        # sort, then increment right until unique than left (2 pointers)

        nums.sort() # tbd if can do efficiently

        l, r = 0, 1
        s = set()
        count = 0
        while r < len(nums):
            if nums[l] not in s:
                s.add(nums[l])

            if nums[r] == nums[l]:
                count += 1
                nums[r] = nums[l] + 1
            elif nums[r] in s:
                count += nums[l] + 1 - nums[r]
                nums[r] = nums[l] + 1 # invariant is can't be in yet
                count 
            l += 1
            r += 1
        
        return count