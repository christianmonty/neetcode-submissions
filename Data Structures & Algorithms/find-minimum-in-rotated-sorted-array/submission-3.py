class Solution:
    def findMin(self, nums: List[int]) -> int:
        #idea: compare first and last element, whichever is less explore that half. Keep going until find min

        f = 0
        l = len(nums)-1

        while f < l:
            if f == l-1:
                return min(nums[f], nums[l])
            mid = (l-f)//2 + f
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[l] < nums[mid]:
                f = mid
            elif nums[f] > nums[mid]:
                l = mid
            else: #implicitly, regular binary search
                l = mid
        return min(nums[f], nums[l])