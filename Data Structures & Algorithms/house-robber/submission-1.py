class Solution:
    def rob(self, nums: List[int]) -> int:
        # attempt at solution done on in-place data

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                continue;
            elif i == len(nums) - 2:
                nums[i] = max(nums[i], nums[i+1])
            else:
                nums[i] = max(nums[i], nums[i+1], nums[i] + nums[i+2])
        
        return nums[0]