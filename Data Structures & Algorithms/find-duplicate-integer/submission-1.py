class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # pwtf is negative marking solution?
        #wait my intuition was right w fast & slow pointers
        # I missed the gist, it's that index values are stored in indexes! Duh. But why does this work?

        # just copied below to practice, delete to practice again from scratch!!
        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        



