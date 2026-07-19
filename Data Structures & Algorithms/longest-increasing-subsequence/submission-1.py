class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size

        if not dp:
            return 0
        dp[size-1] = 1
        maxval = dp[size-1]

        index = size - 2
        while index >= 0:
            best = 1
            j = index + 1
            while j < size:
                if nums[index] < nums[j]:
                    temp = 1 + dp[j]
                    if temp > best:
                        best = temp
                j += 1
            dp[index] = best
            if best > maxval:
                maxval = best
            index -= 1
        
        return maxval
        