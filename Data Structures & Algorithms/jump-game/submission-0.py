class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        j = size-1
        i = j - 1

        if not nums:
            return True #trivially

        if size < 2:
            return True

        while i >= 0:
            if nums[i] < j - i:
                i -= 1
            else:
                j = i
                i -= 1
        if j > 0:
            return False
        return True