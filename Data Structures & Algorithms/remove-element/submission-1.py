class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0

        while l <= r:
            if nums[l] != val:
                l += 1
            else: # meaning nums[l] == val
                if nums[r] != val:
                    nums[l] = nums[r]
                    nums[r] = val
                    l += 1
                r -= 1
            
        return l