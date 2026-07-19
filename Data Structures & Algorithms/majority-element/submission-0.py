class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # one idea to solve in linear time is to track first most, and next most, so O(1) storage
        # issue is pathological case is 1212123333333

        # brute force ways are: 1. Hashmap w/count, 2. Sorting and middle eleemnt
        # how can we do linear time, and O(1) space

        newn = sorted(nums)
        n = len(nums) - 1
        midn = n // 2

        return newn[midn]

        