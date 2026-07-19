class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)

        ssum = tsum = 0
        for i in range(0, size):
            ssum += i
            tsum += nums[i]
        ssum += size
        return ssum - tsum
