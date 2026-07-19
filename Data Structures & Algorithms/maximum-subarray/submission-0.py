class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        best = temp = nums[0]

        for index, item in enumerate(nums):
            if index > 0:
                temp = max(item, item + temp)
                if temp > best:
                    best = temp
        return best


        