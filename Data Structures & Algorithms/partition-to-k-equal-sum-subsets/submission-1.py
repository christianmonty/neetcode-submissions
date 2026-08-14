class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # key hint can do backtracking is that nums.length <= 16 (small!)

        # first let's brute for design solution, then we can optimize to run faster
        # seems same 3 optimizations of Matchsticks to Swuares. 1. reverse sort
        # 2. only test path if not already too large 3. If 0 path not worked, other won't either

        # we don't actually need the specific number in the subset, just the sum. Key idea
        subsets = k * [0]
        total = 0
        nums = sorted(nums, reverse=True)
        for n in nums:
            total += n
        if total % k != 0:
            return False
        ssum = total / k

        def backtrack(index: int) -> bool:
            if index == len(nums):
                for s in subsets:
                    if s != ssum:
                        return False
                return True
            
            for i in range(k):
                if subsets[i] + nums[index] <= ssum:
                    subsets[i] += nums[index]
                    ret = backtrack(index+1)
                    subsets[i] -= nums[index]
                    if ret:
                        return True
                if subsets[i] == 0:
                    break
            return False

        return backtrack(0)
