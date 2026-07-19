class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tricky tricky, first do fast/slow to meet in the loop, then begin at front and keep going to loop begin

        slow = fast = 0

        # wait, point is not to mod around edges. Just do actual numbers as indices
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow

        #fast moves ahead by one at a time
