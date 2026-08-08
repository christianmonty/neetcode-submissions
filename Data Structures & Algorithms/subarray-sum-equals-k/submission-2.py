from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # copied solution is that need a hashmap of prefix sums
        # count each prefix sum, by the end all of them that == k will have count in hm
        # return those with hm[k]
        # maintain count of earlier positions that have prefix sum = currentPrefixSum - k
        # since it implies the numbers in between add to k. constants are currentSum and prefixsum
        count = 0
        res = 0
        hm = defaultdict(int)
        hm[0] = 1 # empty prefix, if first letter == k

        for n in nums:
            res += n
            diff = res - k
            if diff in hm:
                count += hm[diff]
            hm[res] += 1 # or something like hm.get(res, 0) += 1
        return count







        '''
        # while this is correct, it's inefficient for large N so Neetcode failed it

        # one way of doing this is like backtracking generate all subsets, then at end, do sum function on list
        # issue here is nums.length must be <= 20,000 so might be too computationally expensive
        # wait, it must be contigous (not any subset) so we must try something else
        # guess you can hash the tuple (a:b) to say that's counted
        # oh to solve this in O(n^2) with O(n^2) space seems doable?

        hm = {} # to store all the prefix nsums
        count = 0
        # add one item to all sums as next prefix
        # one hs for all prefix sums, another for unique ones?
        # wait we don't need unique since i and j always unique...

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # edge case: j == i + 1
                val = nums[j]
                if j == i:
                    hm[(i, j)] = val
                else:
                    hm[(i,j)] = hm[(i, j-1)] + val
                if hm[(i,j)] == k:
                    count += 1
        return count
        '''





        # What is the "prefix sum" method?
        