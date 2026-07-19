class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # invariant I see here is one half of the rotated array must be cleanly sorted
        # so it's like binary search but we first find sorted half and check if num in there, if is, easy. If not, we keep going.
        # one half will be sorted until the end

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] > nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[left]:
                while left <= mid and nums[left] == nums[mid]:
                    left += 1
            else:
                while right >= mid and nums[right] == nums[mid]:
                    right -= 1
        
        return False