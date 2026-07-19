class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for item in nums:
            if item in hset:
                return True
            hset.add(item)
        return False