class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:

        # looks like we just need prefix and suffix sum arrays here
        # this ofc will be a O(n) implementation
        pre = [0] * len(nums)
        suf = [0] * len(nums)

        for i, val in enumerate(nums):
            if i == 0:
                pre[i] = val
            else:
                pre[i] = pre[i-1] + val

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suf[len(nums)-1] = nums[i]
            else:
                suf[i] = suf[i+1] + nums[i]
        
        mmax = nums[0]
        for i in range(len(nums)):
            mmax = max(mmax, suf[i], pre[i])
        
        return mmax

