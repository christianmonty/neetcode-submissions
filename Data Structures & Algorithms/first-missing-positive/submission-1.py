class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

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
        


        