class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # one way of doing this is start with middle
        # if > before and > after, return that index
        # otherwise move in direction of higher peak
        # what about edge cases of 1 element or 2 elements

        def binSearch(l: int, r: int) -> int:
            mid = (r + l) // 2
            lower = mid - 1
            more = mid + 1
            if lower >= 0 and nums[lower] > nums[mid]:
                return binSearch(l, lower)
            elif more <= len(nums) - 1 and nums[more] > nums[mid]:
                return binSearch(more, r)
            else:
                return mid
        
        return binSearch(0, len(nums))
        
