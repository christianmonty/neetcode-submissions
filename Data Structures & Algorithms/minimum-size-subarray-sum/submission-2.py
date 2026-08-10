import math # tbd needed

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # we know sliding window pattern
        # if subarray is smaller than target, move right forward
        # now if sum == target or greater, compare len r - l with minlen
        # if sum > target, try reducing l or r whichever is smaller to preserve max value for min len
        # then if < target, move right forward
        # if right moves past end and no minlen is found, return 0

        minlen = float('inf')
        l = r = 0
        ssum = 0
        while r < len(nums):
            ssum += nums[r]
            while l <= r and ssum >= target:
                if (r - l) + 1 < minlen:
                    minlen = (r - l) + 1
                ssum -= nums[l]
                l += 1
            r += 1

            
        if minlen == float('inf'):
            return 0
        return minlen