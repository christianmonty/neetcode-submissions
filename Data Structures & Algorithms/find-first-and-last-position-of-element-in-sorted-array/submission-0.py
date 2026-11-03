class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # try to find element near middle, otherwise move left or right accordingly
        # then once find element, could have binary search that tries both sides anyway, if return False, move left that amount, if returns True, then keep full range or sometthing

        # if mid matches, try call left and right. If both True, return their middle index. else return -1
        # if middle index returned, then mark left as that, right as that and then recurse again into far left & far right
        # could say recurse(l: int, r: int, left: bool) and if so keep checking left most. Vice versa for rightmost

        # first figure out if number exists at all, then we'll start from that index expanding outwards both ways
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if index == -1:
            return [-1, -1]

        def recurse(l: int, r: int, left: bool) -> int: # for index it finds or -1
            if l > r:
                return -1
            mid = (l + r) // 2
            val = nums[mid]
            ret = -1

            if val < target:
                return recurse(mid + 1, r, left)
            elif val > target:
                return recurse(l, mid - 1, left)
                
            if left:
                ret = recurse(l, mid - 1, True)
            else:
                ret = recurse(mid + 1, r, False)
            if ret != -1:
                return ret # this prioritizes left or rightmost elements

            if val == target:
                return mid
                
            return ret # as -1


        leftend = recurse(0, index, True)
        rightend = recurse(index, len(nums)-1, False)
        return [leftend, rightend]