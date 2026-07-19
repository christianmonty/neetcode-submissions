class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binS(l: int, r: int) -> int:
            if l > r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binS(l, mid-1)
            else:
                return binS(mid+1, r)
        
        return binS(0, len(nums)-1)