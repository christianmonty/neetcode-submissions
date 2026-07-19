class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = i = 0

        if not nums:
            return None
        
        j = nums[i]
        if len(nums) == 1:
            return 0

        if i + j > len(nums):
            return 1

        while i < len(nums):
            j = min(nums[i], len(nums) - 1 - i)
            jumps += 1

            if i + j == len(nums) - 1: #we're done, found end. Already incremented
                break
            
            maxjump = i + j
            
            for index in range(i+1, maxjump):
                if index + nums[index] > i + j and index + nums[index] >= maxjump:
                    if (index + nums[index] < len(nums) and nums[index + nums[index]] != 0) or index + nums[index] >= len(nums):
                        maxjump = index + nums[index]   
            i = maxjump

        return jumps



        """
        #incomplete attempt to do this backwards via greedy
        if not nums:
            return None

        jumps = 0
        size = len(nums)
        j = 0
        i = size - 2
        while i >= 0:
            if i + j == size - 1:
                j = 0
            jumps += 1
            j += 1
            if nums[i] > 1 and nums[i] >= j:
                jumps -= (j - 1)
                j = 0
            i -= 1

        return jumps
        """