class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        # edge case: nums[0] > lower. or nums[end] < upper
        # empty nums.. then must add all

        i = 0
        outlist = []

        if not nums:
            outlist.append([lower, upper])
            return outlist

        if lower < nums[0]:
            outlist.append([lower, nums[0] - 1])

        while i < len(nums):
            temp = nums[i]
            if i < len(nums) - 1:
                j = i + 1
                temp2 = nums[j]
                if temp2 > temp + 1:
                    outlist.append([temp + 1, temp2 - 1])
            i += 1
        
        if nums[len(nums) - 1] < upper:
            outlist.append([nums[len(nums)-1] + 1, upper])
            
        return outlist