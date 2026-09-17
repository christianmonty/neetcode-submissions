class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # different ways could do it:
        # 1. use sort function, or manual mergesort etc.
        # 2. two pointers like O(n^2) sort seems best
        # 3. how would we do one-pass algo w/only constant extra space?

        # below is idea for O(300) extra space since nums.length is bounded
        # then we just count # 0's, 1's and 2's

        z = 0
        o = 0
        t = 0

        for n in nums:
            if n == 0:
                z += 1
            elif n == 1:
                o += 1
            else:
                t += 1

        k = 0
        while k < len(nums):
            if z:
                nums[k] = 0
                z -= 1
            elif o:
                nums[k] = 1
                o -= 1
            else:
                nums[k] = 2
                t -= 1 # for completeness

            k += 1


        '''
        # below works, but is too much runtime O(n^2)

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        '''
