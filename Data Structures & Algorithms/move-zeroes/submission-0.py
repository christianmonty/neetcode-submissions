class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # left pointer tracks 0 spot
        # right pointer goes to non-zero to flip

        z = 0
        n = 0

        while z < len(nums) and n < len(nums):
            if z == n and nums[z] != 0:
                z += 1
                n += 1
                continue
            while z < len(nums) and nums[z] != 0:
                z += 1
            while n < len(nums) and nums[n] == 0:
                n += 1
            if z < len(nums) and n < len(nums):
                temp = nums[z]
                nums[z] = nums[n]
                nums[n] = temp
            n += 1
            z += 1
        