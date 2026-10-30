from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # trick is need to use custom comparator in cmp_to_key which I didn't know how to do
        # 

        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1: # order should be flipped
                return -1
            else:
                return 1

        # memorize this custom sorting comparator
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))

            

        



        '''
        # we basically need to sort on first digit, and then if tied second digit but empty is > 0
        # 3 > 30-32 but not 33 and beyond
        # we could hash first digit from 9 to 0...and then from there

        # below is my first attempt, but need to use custom comparator
        chars = [str(n) for n in nums]
        chars.sort(reverse=True)
        endstring = ""
        for c in chars:
            endstring = endstring + c

        return endstring
        '''
        