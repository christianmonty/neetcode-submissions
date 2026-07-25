class Solution:
    def removeDuplicates(Self, nums: List[int]) -> int:

        # let's try with 2 pointers. left pointer is where to insert, right pointer moves fwd until non-unique
        # we don't care about second half, it is literally discarded

        l = 1
        r = l + 1
        last = -101

        while l < len(nums):
            if nums[l] <= nums[l-1]:
                # found insertion point
                while r < len(nums) and (nums[r] == nums[l] or nums[r] == last):
                    r += 1
                if r >= len(nums):
                    break
                nums[l] = nums[r]
                last = nums[r]
                r += 1
                '''
                if r >= len(nums) - 1:
                    return l + 1
                '''
            l += 1
        
        return l # will be # of unique elements


'''
        # one idea to do this with 3 pointers
        # if 1st == 2nd, but 3rd greater copy 3rd into second, inc unique by 1, then move all 3 pointers forward by one
        # if 1, 2 and 3 all equal, move all forward by one
        # could use hashset for now to track # unique
        # should be if the leftmost is unique meaning first time seen

        f, s, t = 0, 1, 2
        hs = set()
        count = 0

        while t < len(nums):
            if nums[f] not in hs:
                count += 1
                hs.add(nums[f])
            if nums[f] == nums[s]:
                while nums[t] == nums[s] and t < len(nums) - 1:
                    t += 1
                nums[s] = nums[t]
                if nums[s] not in hs:
                    count += 1
                    hs.add(nums[s])
            f += 1
            s = f + 1
            t += 1
        
        return count
'''
            