class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #is this just returning index of mid if it exists, and -1 if not?
        left, right = 0, len(nums)-1
        if len(nums) < 4:
            for index, value in enumerate(nums):
                if value == target:
                    return index
            return -1

        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1