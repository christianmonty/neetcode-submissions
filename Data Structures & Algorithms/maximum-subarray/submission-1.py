class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        best = -1001
        temp = 0
        for idx, val in enumerate(nums):
            temp = max(val, temp + val)
            best = max(temp, best)
        
        return best