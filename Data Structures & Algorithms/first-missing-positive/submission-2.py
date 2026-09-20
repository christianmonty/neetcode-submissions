class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Negative Marking example - O(N) time and O(1) space per LC Hard

        n = len(nums)

        for index, val in enumerate(nums):
            if val < 0:
                nums[index] = 0

        for index in range(len(nums)):
            val = abs(nums[index])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (n+1)

        for index, val in enumerate(nums):
            if val >= 0:
                return index + 1
        return n + 1






        '''
        # smallest positive integer not present in nums is something between 0 and first pos int
        # or 1 + max pos int if in order
        hs = set()
        mmax = 0
        for n in nums:
            if n > 0:
                hs.add(n)
            if n > mmax:
                mmax = n
        
        for i in range(1, mmax + 1):
            if i not in hs:
                return i
        return mmax + 1
        '''
        


        