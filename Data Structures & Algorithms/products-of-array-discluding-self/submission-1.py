class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zerocount = 0
        for i in nums:
            if i == 0:
                zerocount += 1
            else:
                total *= i
        if zerocount > 1:
            total = 0
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(total)
            elif zerocount > 0:
                output.append(0)
            else:
                output.append(total // nums[i])
        return output