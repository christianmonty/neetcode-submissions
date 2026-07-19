class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None

        size = len(nums)
        dp = [0] * size
        dpo = [0] * size

        dp[size-1] = nums[size-1]
        dpo[size-1] = 0

        if size > 1:
            dp[size-2] = max(dp[size-1], nums[size-2])
            dpo[size-2] = nums[size-2]

        i = size - 3
        while i >= 0:
            if i == 0:
                dp[0] = max(nums[0] + dpo[2], dp[1])
            else:
                dpo[i] = max(nums[i] + dpo[i+2], dpo[i+1]) #like normal
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            i -= 1
        
        return dp[0]
        
