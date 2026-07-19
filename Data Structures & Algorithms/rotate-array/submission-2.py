class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # must not forget when k > len(n)
        k %= len(nums)
        
        for i in range(k):
            temp = nums[0]
            for j in range(len(nums)):
                if j > 0:
                    swap = nums[j]
                    nums[j] = temp
                    temp = swap
            nums[0] = temp
                    