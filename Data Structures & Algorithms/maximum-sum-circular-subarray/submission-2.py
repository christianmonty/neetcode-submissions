class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Had right intuition here for Kandane's algorithm, but looked at solution for specifics

        # trick here is Kandane's algorithm for no wraparound
        # but if wraparound, take total sum - min subarray from Kandane's
        # edge case of all negative numbers, take closest to 0

        curmin = curmax = 0 # since being added to current value in iteration below
        gmin = gmax = nums[0]
        total = 0

        for n in nums:
            curmax = max(curmax + n, n)
            gmax = max(gmax, curmax)
            curmin = min(curmin + n, n)
            gmin = min(gmin, curmin)
            total += n

        return max(gmax, total - gmin) if gmax > 0 else gmax



        '''
        # WOULD THIS BELOW IDEA HAVE WORKED AS DESCRIBED? CHECK...!
        # here's an idea, it's kind of the prefix/suffix pattern
        # so we first do dp as if max subarray sum, heading in right direction
        # and each item either add self to previous sum, or drop to only include self (max of these)
        # and then same heading to the left. Then we have 2 directions
        # then each item, max subarray sum is from left + from right - individual item value
        # to remove the effect of double counting. 
        # how can we ensure we don't overlap both ways? Maybe store in dp further index?
        # imagine all positive numbers, then wouldn't want to count in both direction!

        



        # below is first attempt for reference...


        # is this even greedy? If so, how???

        # Try cleaning up the below mess...

        mmax = sum = 0
        left = None

        for index, val in enumerate(nums):
            if sum == 0:
                if val > 0: # ready to revive
                    sum += val
                    left = index # set left to new
                # else are just skip negatives not needed
            # if val positive, may have new max. If val negative, won't have max but may be worth taking
            else:
                sum += val
                if sum < 0:
                    sum = 0
                    left = None # reset left
            if sum > mmax:
                mmax = sum

        # what if every max, we start a new left point at end of max

        if sum > 0 and left:
            index = 0
            while index < left:
                sum += nums[index]
                if sum > mmax:
                    mmax = sum
                index += 1
        
        
        return mmax



        # right away subarray makes me think sliding window or greedy
        # one idea is we try 3 different ways. best from left, best from right, best from ends?
        # first is like, at each step can add to prev, can reset to 0. Best from left will be found
        # same logic for best from right. Wait this logic is missing 4 -5 9 which is better than not

        # we could throw the modded index into hashset to ensure didn't see already. Or just track somewhere as beginning somehow
        # maxSum would mean when goes negative, start over. Once positive, that's new beginning... (greedy)
        # and basically want to accumulate all the positive, compare to max and make sure don't look around

        # 1. if sum == 0, add value in nums. If positive, then start left as current index.
        # if sum goes negative, reset to 0, clear left. Then keep going at end of array
        # when sum > 0, if greater than new max then update max
        # this is if have 1 single positive number, don't need any of the negative numbers
        # but if all negative numbers, then max sum is just the smallest??
        # if you reach the final index, and count is 0, return min
        # otherwise if count positive, then continue to the left until get to one before left

        '''
