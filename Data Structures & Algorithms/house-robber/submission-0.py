class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)

        dp = [0] * size
        dp[size - 1] = nums[size - 1]
        if size > 1:
            dp[size-2] = max(nums[size-2], nums[size-1])
        
        i = size - 3
        while i >= 0:
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            i -= 1

        return dp[0]