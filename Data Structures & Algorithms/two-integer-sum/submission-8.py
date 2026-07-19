class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = set()
        for i in nums:
            temp = target - i
            if temp in values:
                l1 = nums.index(i)
                l2 = nums.index(temp)
                if l2 < l1:
                    l3 = l1
                    l1 = l2
                    l2 = l3
                elif l2 == l1:
                    l2 = nums.index(i, l1 + 1)
                return [l1, l2]
            values.add(i)