class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        # could sort and check
        # could use set to check duplicates but then how to check consecutive? Track min

        nums.sort()

        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i] or nums[j] != nums[i] + 1:
                return False
            j += 1
            i += 1

        return True
