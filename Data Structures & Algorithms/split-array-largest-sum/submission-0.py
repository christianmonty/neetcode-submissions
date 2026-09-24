class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] + prefix[i] # push one forward

        dp = {}


        def recurse(start: int, end: int, newk: int) -> int:
            if newk <= 1:
                dp[(start, end, newk)] = prefix[end] - prefix[start]
                return dp[(start, end, newk)]
            if (start, end, newk) in dp:
                return dp[(start, end, newk)]
            
            largsum = float("inf")
            for j in range(start + 1, end):
                l = recurse(start, j, 1)
                r = recurse(j, end, newk - 1)
                tempsum = max(l, r)
                largsum = min(largsum, tempsum)
            dp[(start, end, newk)] = largsum
            return largsum
        
        return recurse(0, len(nums), k)
            

                # peeked hint at to use Prefix Sum below & DP

        # could do dp(start index, newk) and see if that has been called before
        # if left to k == 1 or have to calculate subset sum, use prefix sum
        # but where is the binary search? I guess intent is that when split, want to keep min sum of subarray for every split, which means nearly even splits in value
        # so binary search is by value, start in middle, if < half value, try right half, else left
        # but this only works for single split at top level or splits by powers of 2
        # vs. if say k == 3, then need to split into 3 evenly sized chunks so how does bin search help us at all here?

        

        
        # you could binary search on a portion, and return the specific sum
        # so base case is return single element, and then one above that returns sum of both
        # maybe we dp the # of splits and left and right barrier too?
        # binary search should mean roughly half each time though right??

        # Ohh maybe we use prefix sum to then split binary around halfway in terms of sum?
        # but what about one layer deeper, oo then we do prefix sum to r - prefix sum to l...
        '''
        # this recursion means left end, right end and return val
        def recurse(splits: int, left: int, right: int) -> int:
            if left == right:
                return nums[left] # what about if splits are 0, or > 1??
                # or just assume caller would only call with >= 1 split...?
            # otherwise, try all splits and return min? pass to call # splits - 1 to split recursively
        '''



