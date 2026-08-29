class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        hm = {} # cleaner than 2D array
        # hash tuple of (sum, index) = # of ways to reach target from that point

        # can refactor to make run cleaner

        # key thing is must utilize every single element, can't just return when at target
        def recurse(sum: int, index: int) -> int:
            if index == len(nums):
                if sum == target:
                    return 1
                return 0
            if (sum + nums[index], index + 1) in hm:
                ret1 = hm[(sum + nums[index], index + 1)]
            else:
                ret1 = recurse(sum + nums[index], index + 1)
                hm[sum + nums[index], index + 1] = ret1
            
            if (sum - nums[index], index + 1) in hm:
                ret2 = hm[(sum - nums[index], index + 1)]
            else:
                ret2 = recurse(sum - nums[index], index + 1)
                hm[(sum - nums[index], index + 1)] = ret2
            return ret1 + ret2

        return recurse(0, 0)
        