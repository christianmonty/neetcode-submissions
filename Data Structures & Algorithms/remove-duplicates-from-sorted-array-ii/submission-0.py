class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # having peeked at solution, a cleaner approach to solve it
        write = 2

        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]: # found viable thing to write
                nums[write] = nums[read] # place new item
                write += 1
        return write


        # have left pointer advance unti third in a duplicate, then have 2nd ptr advance from 1 fwd
        # and then what....and then keep moving item into left, right increases, left increases


        # below didn't work, was overcomplicated
        '''

        l1 = l2 = r1 = r2 = -10001

        i = j = 0
        while i < len(nums):
            l2 = l1
            l1 = nums[i]
            if nums[i] == l1 == l2:
                # must replace here
                j = max(i + 1, j)
                while j < len(nums):
                    r2 = r1
                    r1 = nums[j]
                    if nums[j] == r1 == r2:
                        j += 1
                    else:
                        nums[i] = nums[j]
                        break
                if j >= len(nums):
                    break
            else:
                i += 1

        return i
        '''